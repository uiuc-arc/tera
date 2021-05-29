import multiprocessing
class Config:
    def __init__(self):
        # Test Driver config
        self.MODE = "CONV"


        self.DEFAULT_ITERATIONS = 30
        self.SUBSEQUENT_ITERATIONS = 30
        self.MAX_ITERATIONS = 500


        self.MAX_DEVIATION_GEWEKE = 1.0
        self.RHAT_THRESHOLD = 1.1

        self.THREAD_COUNT = 1

        self.PROBABILITY_OF_FAILURE = 0.01
        # enables probability update is the original test failure probability is above min threshold
        self.ENABLE_PROB_UPDATE = False
        self.BOUNDS_DELTA = 1
