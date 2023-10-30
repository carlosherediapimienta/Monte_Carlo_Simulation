###############################################################################
######                       DISTRIBUTION SAMPLINGS                        ####
###############################################################################

# Developer: Carlos Heredia Pimienta, University of Barcelona

import numpy as np

class RandomSampling:
    
# Sampling uniform distribution
    def uniform(self, random_number, a, b):
        x = a + random_number*(b-a)
        return x
    
# Sampling exponential distribution
    def exponential(self, random_number, a):
        x = - a*np.log10(random_number)
        return x

# Sampling Wentzel distribution
    def wentzel(self, random_number, a):
        x = (a*random_number)/(a+1-random_number)
        return x