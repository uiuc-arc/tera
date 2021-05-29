import multiprocessing
import os
import re
import numpy as np
import ast

from CompareDistribution import CompareDistribution
from Logger import Logger
from SpecReader import SpecReader
from src.Config import Config
from src.SamplesEvaluator import SamplesEvaluator
from src.Util import sample_to_str, compute_max_diff
from src.lib.AssertType import AssertType
from src.runner.BaseRunner import BaseRunner
import traceback as tb

class StocRunner(BaseRunner):
    HALF_FAILED = 1
    TIMEOUT = 2
    EXCEED_PROBABILITY = 3
    OK = 4

    def __init__(self, spec: SpecReader, condaenvname, libdir, rundir, logstring, logger: Logger, config: Config):
        super().__init__(spec, condaenvname, libdir)
        self.config=config
        self.parallel = True
        self.rundir = rundir
        self.logstring=logstring
        self.logger=logger

    def update_max_failure_probability(self, new_prob):
        self.logger.logo("Updating probability of failure to: {0}".format(new_prob))
        self.config.PROBABILITY_OF_FAILURE = new_prob


    def run_test_wrapper(self, i):
        if self.exec_timeout is not None:
            self.logger.logo("Iter {0}... (timeout = {1})".format(i, self.exec_timeout))
        else:
            self.logger.logo("Iter %s..." % i)
        return self.run_test(i)

    @staticmethod
    def _write_results(results, base_iters, resultdir):
        for i in range(base_iters, base_iters+len(results)):
            with open(os.path.join(resultdir, 'output_{0}'.format(i)), 'w+', encoding='utf-8') as outfile:
                outfile.write(results[i-base_iters][0].decode("utf-8"))
                outfile.write(results[i-base_iters][1].decode("utf-8"))

    def _parse_output(self, out, err):
        try:
            matched = re.findall("{0}[a-zA-Z_]*([0-9.eE+,\[\]\(\) -]+)".format(self.logstring), str(out))

            if len(matched) == 0:
                matched = re.findall("{0}[a-zA-Z_]*([0-9.eE+,\[\]\(\) -]+)".format(self.logstring), str(err))


            values = [np.array(ast.literal_eval(x)) if ('[' in x or '(' in x) else float(x) for x in matched]
            # if len(matched) > 0:
            #     values = [float(m) for m in matched]
            # else:
            #     # may be its array
            #     matched=re.findall("{0}([\[\]0-9.,eE+ -]+)".format(self.logstring), str(out))
            #     values=[np.array(ast.literal_eval(m)) for m in matched]
            assert len(values) >= 2
            if len(values) >= 2:
                actual = np.array([values[i] for i in range(0, len(values), 2)])
                expected = np.array([values[i] for i in range(1, len(values), 2)])
                values = [actual, expected]
            return values, 0
        except:
            self.logger.logo('Not found ::: ')
            return [np.finfo(np.float32).min, np.finfo(np.float32).min], 1

    @staticmethod
    def _append_samples(file, samples):
        with open(file, 'a') as samplefile:
            for sample in samples:
                # writing actual and expected
                for i in range(0, len(sample), 2):
                    samplefile.write("%s::%s\n" % (sample_to_str(sample[i]), sample_to_str(sample[i + 1])))

    def mp_handler(self, data):
        # default thread behaviour
        self.logger.logo("Launching %d jobs, %d in parallel" % (len(data), self.config.THREAD_COUNT if self.parallel else 1))
        with multiprocessing.Pool(self.config.THREAD_COUNT if self.parallel else 1) as p:
            results = p.map(self.run_test_wrapper, data)
        return results

    # returns (All passed, Probability of failure, runtime)
    def run_with_param(self, params, exec_timeout, cur_best_timeout):
        self.save_temp()
        self.exec_timeout=exec_timeout
        # set parameter
        for param in params.keys():
            if param == "param1":
                self.set_parameter(param, int(params[param]))
            else:
                self.set_parameter(param, params[param])

        self.logdir = os.path.join(self.rundir, "assert_{0}_{1}".format(self.spec.get_hash(), '_'.join([str(params[k]) for k in params.keys()])))
        self.logger.logo("Logdir: %s" % self.logdir)
        if os.path.exists(os.path.join(self.logdir, "report.txt")):
            self.logger.logo("Assertion exists.. exiting... ")
            self.logdir = None  # so that instrumentor does not write the files here
            return
        os.makedirs(self.logdir)

        samplefile_path=os.path.join(self.logdir, 'samples.txt')
        # with open(samplefile_path, 'w+') as samplefile:
        #     samplefile.write("spec")

        # run until convergence
        outputs = []
        extracted_outputs = []
        errors = []
        codes = []
        convergence_scores = []
        timings=[]
        decisions = []
        parse_errors=[]
        sampling_iterations = 0
        next_batch_iterations = self.config.DEFAULT_ITERATIONS
        while sampling_iterations < self.config.MAX_ITERATIONS:
            # run the test N times
            results=self.mp_handler(list(range(next_batch_iterations)))
            self._write_results(results, sampling_iterations, self.logdir)
            # collect results
            newsamples=[]
            for r in results:
                outputs.append(r[0])
                timings.append(r[3])  # time in nanoseconds
                parsed_outputs, parse_error=self._parse_output(r[0], r[1])
                parse_errors.append(parse_error)
                newsamples.append(parsed_outputs)
                #extracted_outputs.append(parsed_outputs)
                errors.append(r[1])
                if int(r[2]) != 0:
                    if len(re.findall("1 passed", str(r[0].decode("utf-8")))) == 0:
                        # guarding against spurios failures, like thread failures
                        codes.append(r[2])
                    else:
                        codes.append(0)
                else:
                    codes.append(r[2])
            if sum([x< 10000 for x in timings]) > 0:
                self.logger.logo("Timings: Avg: {0}, Max: {1}, Min: {2}".format(np.mean([x for x in timings if x < 10000]),
                                                                            np.max([x for x in timings if x < 10000]),
                                                                            np.min([x for x in timings if x < 10000])))
            else:
                self.logger.logo("All timed out or failed")
            self.logger.logo("Passed tests : %d" % (sum([int(x)==0 for x in codes])))
            self.logger.logo("Failed tests : %d" % (sum([int(x) != 0 for x in codes])))
            self._append_samples(samplefile_path, newsamples)

            if sum([int(x) != 0 for x in codes]) >= len(codes)/2:
                self.logger.logo("Half of samples failed, exiting...")
                self.restore()
                return False, 1.0, 10000.0, StocRunner.HALF_FAILED
            # update samples in file

            # update samples in list
            extracted_outputs = extracted_outputs + newsamples

            # if assertType is tolerance type, then compute diff and then check convergence
            if AssertType.is_tolerance_assert(self.spec.assertions[0]):
                # compute diff and pass
                samples = [compute_max_diff(extracted_outputs[i][0], extracted_outputs[i][1])
                            for i in range(len(extracted_outputs)) if parse_errors[i] == 0]
            else:
                samples = [extracted_outputs[i][0] for i in range(len(extracted_outputs)) if parse_errors[i] == 0]

            samplesEvaluator = SamplesEvaluator(samples, self.config)
            converged, geweke_score = samplesEvaluator.check_covergence()
            convergence_scores.append(geweke_score)
            self.logger.logo("Converged: %s" % converged)
            self.logger.logo("Convergence score: {0}".format(geweke_score))
            if converged:
                break
            try:
                if np.mean([x for x in timings if x < 10000]) - 1 > cur_best_timeout:
                    self.logger.logo("Exceeding current best timeout: {0} > {1}".format(np.mean([x for x in timings if x < 10000]), cur_best_timeout))
                    return False, 1.0, 10000.0, StocRunner.TIMEOUT
            except:
                self.logger.logo(tb.format_exc())
                pass

            # update iterations
            sampling_iterations += next_batch_iterations
            next_batch_iterations = self.config.SUBSEQUENT_ITERATIONS
            self.logger.logo("Continuing to next batch...")

        self.restore()
        compareDist = CompareDistribution(None,
                                          [extracted_outputs[i][0] for i in range(len(extracted_outputs)) if parse_errors[i] == 0],
                                          [extracted_outputs[i][1] for i in range(len(extracted_outputs)) if parse_errors[i] == 0],
                                          self.spec.assertions[0],
                                          dist_type=None, logger=self.logger)
        self.logger.logo("Evaluating {0} values out of {1}".format(sum([x==0 for x in parse_errors]),len(parse_errors)))
        valid_timings = [x for x in timings if x < 10000]
        if len(valid_timings) > 0:
            self.logger.logo("Overall-timings: Avg: {0}, Max: {1}, Min: {2}".format(np.mean([x for x in timings if x < 10000]),
                                                                        np.max([x for x in timings if x < 10000]),
                                                                        np.min([x for x in timings if x < 10000])))
        else:
            self.logger.logo("All timings timed out")

        prob=compareDist.evaluate()
        if prob > self.config.PROBABILITY_OF_FAILURE:
            self.logger.logo("Exceeding max probability of failure: {0}".format(prob))
            # also sending avg timing for setting original runtime if necessary
            return False, prob, 10000.0, StocRunner.EXCEED_PROBABILITY, np.mean(valid_timings)

        return True, prob, np.mean(valid_timings), StocRunner.OK

