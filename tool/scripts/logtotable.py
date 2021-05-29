import sys
import glob
import os
import numpy as np
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
        self.reduction = 0.0

    def print_spec(self, format='tex'):
        try:
            #reduction = (float(self.original_time) - float(self.best_score))*100.0/float(self.original_time)
            reduction = self.original_time/self.best_score
        except:
            reduction = 1
        self.reduction = reduction
        if format == 'tex':
            sep="&"
            end="\\\\"
        else:
            sep=","
            end=""
        if self.optimizer_time < 60:
            time_format="{0}s".format(int(self.optimizer_time))
        else:
            if self.optimizer_time < 3600: # 1hr
                time_format = "{0}m{1}s".format(int(self.optimizer_time/60), int(self.optimizer_time % 60))
            else:
                time_format = "{0}h{1}m{2}s".format(int(self.optimizer_time/3600), int((self.optimizer_time % 3600) / 60), int(self.optimizer_time%3600) % 60)


        return '{1}{0}{2:.2f}s{0}{3:.2f}s{0}{4:.2f}x{0}{5}{6}'.format(sep, ((self.classname + "::") if self.classname != "none" else "") + self.testname, self.original_time, self.best_score, reduction, time_format, end)

skip=["test_t", "test_beta", "test_sample_posterior_predictive_after_set_data" ,"test_fit_oo[ASVGD-full]"]
specs=[]
logs=glob.glob(os.path.join(sys.argv[1], "**/log.txt"), recursive=True)
#print(logs)
for log in logs:
    with open(log) as file:
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
                if testname in skip:
                    break
            if line.startswith("Original runtime"):
                original_time=line.split(":")[1].strip()
            if line.startswith("Optimizer time"):
                optimizer_time=line.split(":")[1].strip()
            if line.startswith("Best param"):
                best_param="_".join(line.split(" ")[2:])
            if line.startswith("Best score"):
                best_score=line.split(":")[1].strip()
        if original_time is None:
            continue
        specdata=SpecData(repo, classname, testname, float(original_time), float(optimizer_time), best_param, float(best_score), filename)
        specs.append(specdata)
total_original_time=0
total_reduced_time=0
total_reduction=0
for ind in range(len(specs)):
    spec=specs[ind]
    #if spec.classname == "none":
        #print("{0}::{1}".format(spec.filename[spec.filename.index("tests"):], spec.testname))
    #else:
        #print("{0}::{1}::{2}".format(spec.filename[spec.filename.index("tests"):], spec.classname, spec.testname))
    print(spec.print_spec(format='tex').replace("_", "\_"))

    total_original_time+=spec.original_time
    total_reduced_time+=spec.best_score
    total_reduction+=spec.reduction

print("Total&{0:.2f}s&{1:.2f}s&{2:.2f}x\\\\".format(total_original_time, total_reduced_time, total_reduction/len(specs)))






