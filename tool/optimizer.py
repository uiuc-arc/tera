import argparse
import pickle
import subprocess as sp
import time

import libraries
import testspecs
from Logger import Logger
from ParamInstrumentor import ParamInstrumentor
from src import Util
from src.AssertInstrumentor import AssertInstrumentor
from src.Config import Config
from src.Util import create_new_dir
from src.lib import TestSpec
from src.lib.ParamType import ParamType
from src.runner.StocRunner import StocRunner
from src.strategy.bayesopt import BayesOpt


class Optimizer:
    def __init__(self, spec: TestSpec, condaenvname, libdir, logstring, original_time, repo_dir, config:Config):
        self.spec = spec
        self.condaenvname = condaenvname
        self.libdir = libdir
        self.logstring = logstring
        self.original_time = original_time
        self.repo_dir = repo_dir
        self.config = config

    def run_optimizer(self):
        # one dir per repo
        rundir = create_new_dir(repo_dir, "run_")
        logger = Logger(rundir)
        logger.logo(self.spec.get_str())
        logger.logo("Original runtime: {0}".format(self.original_time))
        start = time.time()
        try:
            runner = StocRunner(self.spec, self.condaenvname,
                                libraries.PROJECT_DIR, rundir, self.logstring, logger, self.config)

            paramdict = dict()
            for p in self.spec.params:
                paramdict[p.name] = p
            k = list(paramdict.keys())
            if len(k) == 2 and \
                    (paramdict[k[0]].param_type == ParamType.LR and paramdict[k[1]].param_type == ParamType.ITER or
                     paramdict[k[1]].param_type == ParamType.LR and paramdict[k[0]].param_type == ParamType.ITER):
                bayesopt = BayesOpt(paramdict, runner, logger,
                                    enable_opt=True, enable_timeout=False, enable_prob_update=self.config.ENABLE_PROB_UPDATE)
            elif len(k) == 1 and paramdict[k[0]].param_type == ParamType.ITER:
                bayesopt = BayesOpt(paramdict, runner, logger,
                                    enable_opt=True, enable_timeout=False, enable_prob_update=self.config.ENABLE_PROB_UPDATE)
            else:
                bayesopt = BayesOpt(paramdict, runner, logger,
                                    enable_opt=False, enable_timeout=False, enable_prob_update=self.config.ENABLE_PROB_UPDATE)

            if bayesopt.iter < 0:
                logger.logo("Original test run failed. Exiting...")
                assert False
            result, trialsobj = bayesopt.sample()

            logger.logo("Best param {0}".format(result))
            reduction = ((bayesopt.original_runtime-bayesopt.best_runtime+0.0)
                         * 100.0)/bayesopt.original_runtime
            speedup = bayesopt.original_runtime/bayesopt.best_runtime
            logger.logo("Reduction: {0}%".format(reduction))
            logger.logo("Speedup: {0}x".format(speedup))
            # save trials obj
            with open(rundir+"/trialsobj.pkl", 'wb') as trialsfile:
                pickle.dump(trialsobj, trialsfile, pickle.HIGHEST_PROTOCOL)
        except:
            logger.logo("Exception>>>")
            import traceback
            e = traceback.format_exc()
            logger.logo(e)
        finally:
            end = time.time()
            totaltime = end-start
            logger.logo("Optimizer time: {0}".format(totaltime))


def setup_args(config:Config):
    args = argparse.ArgumentParser(description="Optimizer Arguments")
    args.add_argument("-r", dest="repo", help="Name of repo")
    args.add_argument("-num", help="ID of spec for given repo", type=int, default=-1)
    args.add_argument("-file", help="File name of spec to run")
    args.add_argument("-class", dest='classname', help="Class name of spec")
    args.add_argument("-test", help="Test name of spec")
    args.add_argument("-p", dest="max_prob", type=float, help="Max Probability of Failure",
                      default=config.PROBABILITY_OF_FAILURE)
    args.add_argument("-j", type=int, dest="threads", help="Number of threads", default=config.THREAD_COUNT)
    args.add_argument("-t", type=float, dest="conv_threshold", help="Convergence threshold", default=config.MAX_DEVIATION_GEWEKE)

    return args


def run_pytest(filename, classname, testname, condaenvname, libdir, thread_count):
    # info = resource.getrusage(resource.RUSAGE_CHILDREN)
    result = sp.run(['{4}/tool/src/runtest_original_param.sh {0} {1} {2} {3} {5}'.format(

    #result = sp.run(['time -f "\t%U user,\t%S sys" {4}/tool/src/runtest.sh {0} {1} {2} {3}'.format(
        filename,
        classname,
        testname,
        condaenvname,
        libdir,
        thread_count
    )],
        shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    sys_exec_time_mins = float(str(result.stderr).strip().rpartition('sys')[2].partition('m')[0].rpartition('t')[2])
    sys_exec_time_secs = float(str(result.stderr).strip().rpartition('sys')[2].partition('m')[2].partition('s')[0])
    user_exec_time_mins = float(str(result.stderr).strip().rpartition('user')[2].rpartition('sys')[0].rpartition('m')[0].rpartition('t')[2])
    user_exec_time_secs = float(str(result.stderr).strip().rpartition('user')[2].rpartition('sys')[0].rpartition('m')[2].rpartition('s')[0])

    #sys_exec_time = float(str(result.stderr).strip().rpartition('t')[2].rpartition('sys')[0].strip())
    #user_exec_time = float(str(result.stderr).strip().rpartition('user')[0].rpartition('t')[2].strip())
   # info2 = resource.getrusage(resource.RUSAGE_CHILDREN)
   # total_time = (info2.ru_utime + info2.ru_stime) - \
   #     (info.ru_utime + info.ru_stime)
    # total_time=time.time()-start
    total_time = sys_exec_time_mins * 60 + user_exec_time_mins * 60 + sys_exec_time_secs + user_exec_time_secs
    return result.stdout, result.stderr, result.returncode, total_time

# testspecs=open("testspecs.csv").readlines()


# get default config and update
config = Config()
arg_parser = setup_args(config)
args = arg_parser.parse_args()
config.PROBABILITY_OF_FAILURE = args.max_prob
config.THREAD_COUNT = args.threads
config.MAX_DEVIATION_GEWEKE = args.conv_threshold

# setup optimizer
thread_count = config.THREAD_COUNT
testspecs = testspecs.testspecs
repo_dirs = dict()
count = 0
if args.repo is not None:
    testspecs = list(filter(lambda spec: spec.repo == str(args.repo), testspecs))
    assert len(testspecs) > 0

if args.num >= 0:
    testspecs = testspecs[args.num:args.num+1]

if args.file is not None:
    testspecs = list(filter(lambda x: args.file in x.filename, testspecs))
if args.classname is not None:
    testspecs = list(filter(lambda x: args.classname == x.classname, testspecs))
if args.test is not None:
    testspecs = list(filter(lambda x: args.test == x.testname, testspecs))

for spec in testspecs:
    count += 1
    print("Spec: {0}".format(count))
    if spec.skip:
        print("Skipped")
        continue

    print(spec.testname)
    # get original runtime
    print("Running test...")

    res = run_pytest(spec.filename, spec.classname,
                     spec.testname, spec.repo, libraries.PROJECT_DIR, thread_count)
    runtime_avg = res[3]

    if spec.repo not in repo_dirs:
        repo_dirs[spec.repo] = create_new_dir(
            "{0}/tool/logs".format(libraries.PROJECT_DIR), "optim_", '_' + spec.repo)

    repo_dir = repo_dirs[spec.repo]

    # save file
    Util.save_temp(spec.filename, spec.filename+".bak")

    if spec.assertions[0].test.filename is not None:
        if spec.assertions[0].test.filename != spec.filename:
            Util.save_temp(
                spec.assertions[0].test.filename, spec.assertions[0].test.filename + ".bak")
    try:
        # instrument #1 : replace constant by tag
        paramInstrumentor = ParamInstrumentor(spec)
        paramInstrumentor.instrument()
        
        # instrument #2 : log the assert
        assertInstrumentor = AssertInstrumentor(
            spec.assertions[0], "log>>>", ["numpy", "pytorch"])
        assertInstrumentor.instrument()
        assertInstrumentor.write_file()
        
        # run optimizer and find optimum parameters
        optimizer = Optimizer(spec, spec.repo,
                              libraries.PROJECT_DIR, "log>>>", runtime_avg, repo_dir, config)

        optimizer.run_optimizer()
    except:
        import traceback as tb
        tb.print_exc()
    finally:
    
        Util.restore(spec.filename+".bak", spec.filename)

        if spec.assertions[0].test.filename is not None:
            if spec.assertions[0].test.filename != spec.filename:
                Util.restore(
                    spec.assertions[0].test.filename + ".bak", spec.assertions[0].test.filename)
