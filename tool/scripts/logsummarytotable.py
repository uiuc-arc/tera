import glob
import sys
from tabulate import tabulate
import numpy as np
import scipy.stats as st


class SpecData:
    def __init__(self, repo, classname, testname, original_time, optimizer_time, best_param, best_score, filename):
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


def getspecdata(logfile):
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
            if line.startswith("Optimizer time"):
                optimizer_time=line.split(":")[1].strip()
            if line.startswith("Best param"):
                best_param="_".join(line.split(" ")[2:])
            if line.startswith("Best score"):
                best_score=line.split(":")[1].strip()
        if original_time is None:
            return None

        return SpecData(repo, classname, testname, float(original_time), float(optimizer_time), best_param, float(best_score), filename)

spec_dict = dict()

logs=glob.glob(sys.argv[1] + "/optim_*/")
#print(logs)
for m in logs:
    name=m.split("_")[-1].split("/")[0]
    cur_spec_dict = spec_dict.get(name, [])
    tests = glob.glob(m+"/run_*/log.txt")
    for t in tests:
        s = getspecdata(t)
        if s is not None:
            cur_spec_dict.append(s)

    spec_dict[name] = cur_spec_dict

test_count=0
speedups = []
original_times=[]
optimized_times = []
result_table = []
for k in spec_dict.keys():
    if len(spec_dict[k]) == 0:
        continue
    avg_speedup = st.gmean([x.reduction for x in spec_dict[k]])
    max_speedup = np.max([x.reduction for x in spec_dict[k]])
    speedups = speedups + [x.reduction for x in spec_dict[k]]

    total_original_time = np.sum([x.original_time for x in spec_dict[k]])
    total_optimized_time = np.sum([x.best_score for x in spec_dict[k]])
    original_times.append(total_original_time)
    optimized_times.append(total_optimized_time)
    r = [k, len(spec_dict[k]), "{0:.2f}x".format(avg_speedup), "{0:.2f}x".format(max_speedup),
         "{0:.2f}s".format(total_original_time),
         "{0:.2f}s".format(total_optimized_time)]
    result_table.append(r)
    #print("{0}&{1}&{2:.2f}x&{3:.2f}x&{4:.2f}s&{5:.2f}s\\\\".format(k, len(spec_dict[k]), avg_speedup, max_speedup, total_original_time, total_optimized_time))
    test_count+=len(spec_dict[k])

result_table.append(["Total/Avg", test_count, "{0:.2f}x".format(st.gmean(speedups)), "{0:.2f}x".format(np.max(speedups)),
                     "{0:.2f}s".format(np.mean(original_times)), "{0:.2f}s".format(np.mean(optimized_times))])
#print("\\midrule Total/Avg&{0}&{1:.2f}x&{2:.2f}x&{3:.2f}s&{4:.2f}s\\\\".format(test_count, st.gmean(speedups), np.max(speedups), np.mean(original_times), np.mean(optimized_times)))
print(tabulate(result_table, headers=["Project", "#Tests", "Mean Speedup", "Max Speedup", "Original time", "Optimized time"]))
