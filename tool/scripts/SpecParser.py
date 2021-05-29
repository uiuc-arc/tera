
import numpy as np
import ast


class ParamData:
    def __init__(self):
        self.default_val=None
        self.ptype=None
        self.name=None


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
        self.params = list()

    @staticmethod
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
            trials=0
            passed=0
            failed=0
            paramMode = False
            params = []
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
                if line.startswith("Params:"):
                    paramMode=True
                if line.startswith("Assertion:"):
                    paramMode=False

                if paramMode:
                    newparamdata = line.split(" ")[-1].split(",")
                    newparam = ParamData()
                    newparam.default_val = ast.literal_eval(newparamdata[-1].strip())
                    newparam.ptype = newparamdata[-2]
                    newparam.name = newparamdata[0]
                    params.append(newparam)

            if original_time is None:
                return None

            specData = SpecData(repo, classname, testname, float(original_time), float(optimizer_time), best_param,
                            float(best_score), filename, trials, passed, failed)
            specData.params = params
            return specData