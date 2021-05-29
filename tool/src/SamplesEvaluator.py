import numpy as np
import traceback
import arviz

from src.Config import Config


class SamplesEvaluator:
    def __init__(self, test_samples: list, config: Config):
        self.test_samples = test_samples
        self.config=config
        if isinstance(self.test_samples, list):
            self.test_samples=np.array(self.test_samples)

    def check_covergence(self) -> (bool, float):
        try:
            # if empty return True
            if len(self.test_samples) == 0:
                return True, 0.0

            if isinstance(self.test_samples[0], np.ndarray):
                return self.check_convergence_array()

            #self.test_samples = np.array([np.round(x, 8) for x in self.test_samples])

            # special case for 0 variance
            if (self.test_samples == self.test_samples[0]).all():
                return True, 0.0

            zscores=arviz.geweke(self.test_samples, intervals=int(len(self.test_samples)/2))

            if np.isnan([x[1] for x in zscores]).all():
                print("All nan scores, returning false")
                return False, 0.0
            max_deviation=max([abs(x[1]) for x in zscores if not np.isnan(x[1])])
            #print("Current Geweke score (max deviation) %s" % max_deviation)
            if max_deviation <= self.config.MAX_DEVIATION_GEWEKE:
                return True, max_deviation  # converged
            else:
                return False, max_deviation  # not converged
        except np.linalg.LinAlgError:
            traceback.print_exc()
            print("Too few samples....")
            return False, np.inf
        except Exception as err:
            traceback.print_exc()
            #print(traceback.format_exc())
            return False, np.inf

    def check_convergence_array(self) -> (bool, float):
        # special case, empty arrays
        if len(self.test_samples)==0 or len(self.test_samples[0])==0:
            return True, 0.0

        # the samples are array of ndarrays... check for equality for each position

        positions = list(range(len(self.test_samples[0].flatten())))
        res=[]
        for p in positions:
            samplesEvaluator=SamplesEvaluator([arr.flatten()[p] for arr in self.test_samples if p < len(arr)], self.config)
            res.append(samplesEvaluator.check_covergence())
        combined_result=[r[0] for r in res]
        #print(res)
        return sum(combined_result) == len(res), np.max([r[1] for r in res])



    def check_rhat(self) -> float:
        half=int(len(self.test_samples)/2)
        score=arviz.rhat(np.array([self.test_samples[:half], self.test_samples[half:half*2]]))
        if score < 1.1:
            print("Converged")
        else:
            print("Not converged")
        print('Gelman Rubin: %s' %score)
        return score