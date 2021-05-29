
import sys
import glob
import os
from typing import Dict, List

from tabulate import tabulate
import numpy as np
import ast


class SpecData:
    def __init__(self, repo, classname, testname, original_time, optimizer_time, best_param, best_score, filename, trials, passed, failed):
        self.repo=repo
        self.classname=classname
        self.testname=testname
        self.original_time=original_time
        self.optimizer_time=optimizer_time
        self.best_param = best_param
        self.best_score = best_score
        if self.best_score == np.inf:
            self.best_score = self.original_time
        self.filename = filename
        self.reduction = self.original_time/self.best_score
        self.trials = trials
        self.passed = passed
        self.failed = failed


def getspecdata(logfile) -> SpecData:
    with open(logfile) as file:
        #print(log)
        lines=file.readlines()
        repo=None
        classname=None
        testname=None
        original_time=None
        optimizer_time=None
        best_param=None
        best_score=np.inf
        filename=None
        trials=0
        passed=0
        failed=0
        for line in lines:
            if line.startswith("Repo"):
                repo=line.split(":")[1].strip()
            if line.startswith(("Filename")):
                filename=line.split(":")[1].strip()
            if line.startswith("ClassName"):
                classname=line.split(":")[1].strip()
            if line.startswith("Testname"):
                testname=line.split(":")[1].strip()
            if line.startswith("Original runtime"):
                original_time=line.split(":")[1].strip()
            if line.startswith(">>Setting "):
                original_time=line.split(" to ")[1].strip()
                # resetting
                passed = 0
                failed = 0
                trials = 0
            if line.startswith("Optimizer time"):
                optimizer_time=line.split(":")[1].strip()
            if line.startswith("Best param"):
                best_param=ast.literal_eval(" ".join(line.split(" ")[2:]))
            if line.startswith("Best score"):
                best_score=line.split(":")[1].strip()
            if line.startswith("Best-param"):
                trials+=1
            # if line.startswith("Trials"):
            #     trials=int(line.split(":")[1].strip()) - 1
            if line.startswith("Passed tests"):
                p = int(line.split(":")[1].strip())
                passed += p
            if line.startswith("Failed tests"):
                f = int(line.split(":")[1].strip())
                failed += f

        if original_time is None:
            return None

        return SpecData(repo, classname, testname, float(original_time), float(optimizer_time), best_param,
                        float(best_score), filename, trials, passed, failed)

def get_time_format(optimizer_time):
    if optimizer_time < 60:
        time_format = "{0}s".format(int(optimizer_time))
    else:
        if optimizer_time < 3600:  # 1hr
            time_format = "{0}m{1}s".format(int(optimizer_time / 60), int(optimizer_time % 60))
        else:
            time_format = "{0}h{1}m{2}s".format(int(optimizer_time / 3600), int((optimizer_time % 3600) / 60),
                                                int(optimizer_time % 3600) % 60)
    return time_format


def read_run_schedule():
    sched=dict()
    ll = open(os.path.dirname(os.path.realpath(__file__)) + "/buildtimes.txt").readlines()
    for l in ll:
        sched[l.split(",")[0]] = int(l.split(",")[1])
    return sched


def get_benefit_time(t_opt, original_time, optimized_time, num_builds):
    return t_opt/((original_time-optimized_time)*num_builds)


def get_total_saved_time_per_day(original_time, optimized_time, num_builds):
    t = (original_time-optimized_time)*num_builds
    return t
    if t < 60:
        return "%.2fs" % t
    else:
        return "%.2fm" % (t/60)

spec_dict = Dict[str, Dict[str, List[SpecData]]]
spec_dict = dict()
schedules = read_run_schedule()
logs=glob.glob(sys.argv[1] + "/optim_*/")

for m in logs:
    name=m.split("_")[-1].split("/")[0].split("\\")[0]
    cur_spec_dict = Dict[str, List[SpecData]]
    cur_spec_dict = spec_dict.get(name, [])
    tests = glob.glob(m+"/run_*/log.txt")
    for t in tests:
        s = getspecdata(t)
        if s is not None:
            cur_spec_dict.append(s)

    spec_dict[name] = cur_spec_dict

test_count=0
result_table=[]
for k in sorted(spec_dict.keys()):
    if len(spec_dict[k]) == 0:
        continue
    optimizing_times = [x.optimizer_time for x in spec_dict[k]]
    trials = [x.trials for x in spec_dict[k]]
    param_size = [len(x.best_param.keys()) for x in spec_dict[k] if x.best_param is not None]
    avg_time = np.mean(optimizing_times)
    median_time = np.median(optimizing_times)
    total_runs = [(x.passed+x.failed)/x.trials for x in spec_dict[k] if x.trials > 0]
    original_times = [x.original_time for x in spec_dict[k]]
    saveperday = get_total_saved_time_per_day(np.sum(original_times),
                               np.sum([x.best_score for x in spec_dict[k]]), schedules[k])

    benefit = get_benefit_time(np.sum(optimizing_times),  np.sum(original_times),
                               np.sum([x.best_score for x in spec_dict[k]]), schedules[k])
    benefit20 = get_benefit_time(np.sum(optimizing_times),  np.sum(original_times),
                               np.sum([x.best_score for x in spec_dict[k]]), 20)
    #print("%s,%d,%f" % (k, schedules[k], saveperday))
    result_table.append([k, len(spec_dict[k]), get_time_format(avg_time), get_time_format(median_time),
                         "{0:.0f}".format(np.mean(trials)),
                         "{0:.1f}".format(np.round(np.mean(param_size), 2)),
                         "{0:.2f}".format(np.mean(total_runs)),
                         "{0:.2f}".format(np.mean(original_times))])
    #print("{0}&{1}&{2}&{3}&{4:.0f}&{5:.1f}&{6:.2f}&{7:.2f}s&{8:.1f}d&{9:.1f}d\\\\".format(k, len(spec_dict[k]), get_time_format(avg_time),
    #                                        get_time_format(median_time), np.mean(trials), np.round(np.mean(param_size), 2),
    #                                                            np.mean(total_runs), np.mean(original_times), benefit, benefit20))
    test_count+=len(spec_dict[k])

print(tabulate(result_table, headers=["Project", "#Tests", "Avg Time", "Med Time", "Avg. #Iters",
                                      "Avg. params", "Avg Runs", "Avg Test Run-time"]))
#print("\\midrule Total/Avg&{0}&{1:.2f}x&{2:.2f}x&{3:.2f}s&{4:.2f}s\\\\".format(test_count, np.mean(speedups), np.max(speedups), np.mean(original_times), np.mean(optimized_times)))

