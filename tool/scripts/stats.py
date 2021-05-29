
import ast
import glob
import sys
from typing import Dict, List

import numpy as np


class SpecData:
    def __init__(self, repo, classname, testname, original_time, optimizer_time, best_param, best_score, filename,
                 trials, passed, failed, best_prob):
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
        self.best_prob = best_prob


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
        cur_time = 0
        cur_prob = 0
        cur_best_score = None
        best_prob = -1
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
            if line.startswith("Overall-timings: "):
                cur_time = line.split("Avg: ")[1].split(",")[0].strip()
            if line.startswith("Probabilty of failure"):
                cur_prob = line.split(":")[1].strip()
            if line.startswith("Best-score:"):
                cur_best_score = line.split(":")[1].strip()

                if cur_best_score == cur_time:
                    best_prob = cur_prob
                cur_time =  0
                cur_prob = 0
                cur_best_score = -1

        if original_time is None:
            return None

        return SpecData(repo, classname, testname, float(original_time), float(optimizer_time), best_param,
                        float(best_score), filename, trials, passed, failed, best_prob)

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

# expected runtime1 = (1-p).T_opt + p.(T_opt+T_org)
# expected runtime2 = (1-p).T_opt + p.(1-p)(2T_opt) + p.p.(1-p).(3T_opt) + ...
def compute_expected_runtime(spec_data: SpecData):
    if spec_data.best_prob is None:
        assert False
    if spec_data.best_prob == -1:
        return spec_data.original_time

    prob = float(spec_data.best_prob)
    if prob > 0:
        print(">>",spec_data.testname, prob)
    orig_rt = spec_data.original_time
    opt_rt = spec_data.best_score

    return (1-prob)*opt_rt + prob*(opt_rt+orig_rt)


spec_dict = Dict[str, Dict[str, List[SpecData]]]
spec_dict = dict()

logs=glob.glob(sys.argv[1] + "/optim_*/")

for m in logs:
    name=m.split("_")[-1].split("/")[0]
    cur_spec_dict = Dict[str, List[SpecData]]
    cur_spec_dict = spec_dict.get(name, [])
    tests = glob.glob(m+"/run_*/log.txt")
    for t in tests:
        s = getspecdata(t)
        if s is not None:
            cur_spec_dict.append(s)

    spec_dict[name] = cur_spec_dict


params=dict()
r=[]
for k in spec_dict.keys():

    for test in spec_dict[k]:
        if test.reduction > 1:
            r=r+[test.reduction]
            for p in test.best_param.keys():
                params[p] = params.get(p, 0) + 1
        if test.reduction < 1.1:
            print(test.repo, test.testname, test.best_param, test.reduction)

import scipy.stats as st
print(st.gmean(r))
k=list(params.keys())
k=sorted(k, key=lambda x:params[x], reverse=True)
for kk in k:
    print(kk, params[kk])


#print("\\midrule Total/Avg&{0}&{1:.2f}x&{2:.2f}x&{3:.2f}s&{4:.2f}s\\\\".format(test_count, np.mean(speedups), np.max(speedups), np.mean(original_times), np.mean(optimized_times)))

