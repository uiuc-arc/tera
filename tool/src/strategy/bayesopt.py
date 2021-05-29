import numpy as np
import hyperopt
from hyperopt import hp, tpe, fmin, Trials
from hyperopt.pyll.base import scope

from src.lib.ParamType import ParamType
from src.runner.StocRunner import StocRunner

class BayesOpt:
    def __init__(self, param_config: dict, runner: StocRunner, logger,
                 enable_opt=False, enable_timeout=True, enable_prob_update=False):
        self.param_config = param_config
        self.runner = runner
        self.space = None
        self.results=dict()
        # self.best_score=original_runtime
        # self.best_runtime=original_runtime
        self.best_score = -1
        self.best_runtime = np.inf
        self.original_runtime = None
        self.iter = -1
        self.best_param = None
        self.repeated_params=0
        self.logger=logger
        self.enable_timeout = enable_timeout
        # enables   opt 1: exit on higher iterations
        #           opt 2: exit on lower learning rate - threshold x%
        #           opt 3: set timeout based on best runtime so far
        self.enable_opt = enable_opt
        self.lr_threshold = 0.1
        self.enable_prob_update = enable_prob_update
        self.used_iterations = 0
        self.get_original_runtime()


    def _get_score(self, params: dict):
        s=self._param_to_string(params)
        if s in self.results:
            return self.results[s]
        return None

    def _param_to_string(self, params: dict):
        return '_'.join([p+'_'+str(params[p]) for p in params])

    def compute_score(self, params: dict):
        result=self._get_score(params)
        self.logger.logo("Optimization Iteration: {0}".format(self.iter))
        self.logger.logo("Running with params: {0}".format(params))
        self.iter += 1
        # used existing score
        if result is not None:
            self.repeated_params+=1
            return result

        # do not allow iterations higher than (lowest successful iteration/best score iteration) so far
        if self.enable_opt:
            if self.best_param is not None:
                for p in params:
                    # opt 1
                    if self.param_config[p].param_type == ParamType.ITER and params[p] > self.best_param[p]:
                        self.logger.logo("Higher iteration... returning...")
                        return {"loss": np.finfo(np.float32).max, "status": hyperopt.STATUS_FAIL}

                    # opt 2
                    if self.param_config[p].param_type == ParamType.LR and params[p] - self.best_param[p] + self.lr_threshold*self.best_param[p] < 0:
                        self.logger.logo("Lower learning rate.. returning... Best: {0}, Proposed: {1}".format(self.best_param[p], params[p]))
                        return {"loss": np.finfo(np.float32).max, "status": hyperopt.STATUS_FAIL}

        # run the test with chosen parameters, also allow optimization wrt timeout
        output = self.runner.run_with_param(params, self.best_runtime if self.enable_timeout and self.best_runtime < np.inf else None, self.best_runtime)

        # compute score
        # assign high score if it failed
        # otherwise add probability of failure
        # and runtime estimate (normalized)
        #score = (1-output[0]) * np.finfo(np.float32).max + output[1] + output[2]
        score = (1 - output[0]) * np.finfo(np.float32).max + output[2]
        if self.best_score == -1:
            self.best_score = score
            if score < np.finfo(np.float32).max:
                self.best_param = params
        elif self.best_score > score:
            self.best_score=score
            if score < np.finfo(np.float32).max:
                self.best_param = params

        if output[2] < self.best_runtime:
            self.best_runtime = output[2]

        self.results[self._param_to_string(params)] = \
            {"loss": score, "status": hyperopt.STATUS_FAIL if not output[0] else hyperopt.STATUS_OK}
        self.logger.logo("All-Passed: {0}".format(output[0]))
        self.logger.logo("Probabilty of failure: {0}".format(output[1]))
        self.logger.logo("Runtime: {0}".format(output[2]))
        self.logger.logo("Score: {0}".format(score))
        self.logger.logo("Best-score: {0}".format(self.best_score))
        self.logger.logo("Best-param: {0}".format(self.best_param))
        if len(output) > 4:
            avg_time = output[4]
        else:
            avg_time = -1

        self.used_iterations+=1
        # adding StocRunner code
        return {"loss": score, "status": hyperopt.STATUS_FAIL if not output[0] else hyperopt.STATUS_OK,
                "prob": output[1], "code": output[3], "avg_time": avg_time, "param" : params}

    def define_space(self):
        space=dict()
        for p in self.param_config:
            param=self.param_config[p]
            if param.param_type == ParamType.ITER:
                if param.param_default <= 1000:
                    space[param.name] = scope.int(
                        hp.qloguniform(param.name, np.log(param.value_range[0]),
                                       np.log(param.value_range[-1]),
                                       10 if param.step is None else param.step))
                else:
                    space[param.name] = scope.int(hp.qloguniform(param.name, np.log(param.value_range[0]),
                                                                 np.log(param.value_range[-1]),
                                                                 100 if param.step is None else param.step))
            elif param.param_type == ParamType.LR:
                space[param.name] = hp.loguniform(param.name, np.log(param.value_range[0]), np.log(param.value_range[-1]))
            elif param.param_type == ParamType.CHAINS:
                space[param.name] = hp.choice(param.name, param.value_range)
            else:
                self.logger.logo("Unknown param type", param.param_type)

        self.space = space

    def get_original_runtime(self):
        self.logger.logo(">>Getting original runtime")
        p_dict = {}
        for p in self.param_config:
            param_name = self.param_config[p].name
            p_dict[param_name] = self.param_config[p].param_default
        result = self.compute_score(p_dict)

        if result["status"] != hyperopt.STATUS_OK:
            if "code" in result and result["code"] == StocRunner.EXCEED_PROBABILITY and \
                    "avg_time" in result and result["avg_time"] != -1 and self.enable_prob_update:
                self.logger.logo(">>>!!Warning: Allowing update probability!!<<")
                self.runner.update_max_failure_probability(result["prob"])
                self.original_runtime = result["avg_time"]
                self.best_runtime = result["avg_time"]
                self.best_score = self.best_runtime
                self.best_param = result["param"]
                self.logger.logo(">>Setting original runtime to {0}".format(self.original_runtime))
                self.iter = 1
                return True
            else:
                self.logger.logo("Something failed")
                self.iter = -1
                return False
        self.original_runtime = self.best_runtime
        self.logger.logo(">>Setting original runtime to {0}".format(self.original_runtime))
        self.iter = 1
        return True
        #self.best_score = result[0]


    def sample(self):
        self.define_space()
        trials=Trials()
        prev_best=None
        step=50
        for i in range(50, 5001, step):
            best = fmin(fn=self.compute_score, space=self.space, algo=tpe.suggest, max_evals=len(trials)+step, trials=trials,
                        verbose=True, timeout=6000)
            self.logger.logo("Upto iteration {0}: {1}".format(i, best))
            if best == prev_best:
                self.logger.logo("Breaking...")
                break
            prev_best=best

        self.logger.logo(best)
        self.logger.logo("Best score: {0}".format(self.best_score))
        self.logger.logo("Repeated params: {0}".format(self.repeated_params))
        self.logger.logo("Trials: {0}".format(self.iter))
        self.logger.logo("Used Iterations: {0}".format(self.used_iterations))
        return best, trials
