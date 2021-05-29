from src.strategy.HyperParameter import HyperParameter
from typing import List


class SpaceConfig:
    def __init__(self, hyperparameters:List[HyperParameter]=[]):
        self.hyperparameters = hyperparameters

    def add_hyperparameter(self, hp: HyperParameter):
        self.hyperparameters.append(hp)

    def sample(self, best_params=None):
        return [hp.sample(best_params) for hp in self.hyperparameters]

