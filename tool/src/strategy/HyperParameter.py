from src.lib.ParamType import ParamType
from scipy.stats.distributions import uniform, randint
from scipy.stats import loguniform
from typing import Union
import numpy as np

class HyperParameter:
    def __init__(self, name:str, dist, lb, ub, param_type:ParamType, q=None, casttoint=False):
        self.name = name
        self.dist = dist
        self.lb = lb
        self.ub = ub
        self.q = q
        self.param_type = param_type
        self.casttoint=casttoint

    def sample(self, best_param=None):
        s = None
        lb=self.lb
        ub=self.ub
        if best_param is not None:
            if self.param_type == ParamType.ITER:
                ub=best_param[self.name]
                lb=max(lb, ub-1000)
            elif self.param_type == ParamType.LR:
                lb=max(lb, 10**np.round(np.log10(best_param[self.name])))

        if self.dist == uniform:
            s= uniform(lb, ub-lb).rvs()
        elif self.dist == randint:
            s= randint(lb, ub).rvs()
        elif self.dist == loguniform:
            s = np.exp(loguniform(np.log(lb), np.log(ub)).rvs())
        if self.q is not None:
            s = np.round(s/self.q)*self.q
        if self.casttoint:
            s = int(s)
        return s

    # update hyper-parameter based on recent successful parameter config
    def update(self, params: Union[dict, int, float]):
        val = params[self.name] if isinstance(params, dict) else params
        if self.param_type == ParamType.ITER:
            self.ub = int(val)





