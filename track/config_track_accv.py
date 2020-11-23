"""
Written by Matteo Dunnhofer - 2020

Configuration class for TRAS, TRAST, TRASFUST
"""

class Configuration(object):


    DATA_PATH = '/media/TBData2/data/vot/'
    CKPT_PATH = '/media/TBData2/projects/vot-kd-rl-domain-adapt/experiments/VotRlDemo201910100651-pool/TEST_WORKER_25/ckpt/ActorCriticModel_120000.weights'  # None

    SIZE = [128, 128]
    SEQ_LENGTH = 32
    CONTEXT_FACTOR = 1.5
    LSTM_UPDATE = True

    USE_RESULTS = True
    TRAST_TEACHER = 'ECO'
    TRASFUST_TEACHERS = ['ECO', 'MDNet']
    TRACKER_RESULTS_PATH = './trackers/results'

    USE_GPU = True

    def __init__(self):
        super(Configuration, self).__init__()

