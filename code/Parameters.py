__author__ = 'Sander van Rijn <svr003@gmail.com>'

import numpy as np


class Parameters(object):
    """
        Data holder class that initializes *all* possible parameters, regardless of what functions/algorithm are used
        If multiple functions/algorithms use the same parameter name, but differently, these will be split into
            separate parameters.
    """


    def __init__(self, n, mu, labda):
        self.n = n
        self.mu = mu
        self.labda = labda

        ''' (1+1)-ES '''
        self.success_history = np.zeros((10*n, ), dtype=np.int)
        self.sigma = 1
        self.c = 0.817