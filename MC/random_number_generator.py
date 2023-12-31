###############################################################################
######                        RANDOM NUMBER GENERATOR                      ####
###############################################################################

# Developer: Carlos Heredia Pimienta, University of Barcelona

import pandas as pd

class RandomGenerator:

    def __init__(self):
        try:
            self.df_seeds = pd.read_csv('Data/seeds.txt', delimiter='\t', header=None)
        except FileNotFoundError:
            print("Error: Seed data not found!")
        except Exception as e:
            print(f"Error:{e}")
    
###############################################################################
######                    RANDOM NUMBERS GENERATOR                         ####
###############################################################################

# Information: This code is based on the "FUNCTION RAND (Random number generator)"
# of PENELOPE(2023) , which is based on the subroutine RANECU written by F. James
# (Comput. Phys. Commun. 60 (1990) 329-344). It generates a single random number 
# uniformly distributed in the open interaval (0,1).

    def generate_random_number(self, seed1, seed2):

        # Fixed values:
        uscale = 1.0e0/2.147483563e9

        # Calculations 1:
        I1 = seed1/53668
        seed1 = 40014*(seed1-I1*53668)-I1*12211

        if seed1 < 0:
            seed1 = seed1 + 2147483563

        # Calculations 2:
        I2 = seed2/52774
        seed2 = 40692*(seed2-I2*52774)-I2*3791

        if seed2 < 0:
            seed2 = seed2 + 2147483399

        # Calculations 3:    
        IZ = seed1 - seed2
        if IZ < 1:
            IZ = IZ + 2147483562
    
        # Random number
        random_number = IZ*uscale

        return random_number, seed1, seed2

###############################################################################
######                            SEEDS                                    ####
###############################################################################

# Seeds: The following compilation was generated through the execution of a program 
# authored by Andreu Badal and Josep Sempau [Comp. Phys. Commun. 175 (2006) 440�450]. 
    def  random_seed(self, N):
        if N >= 0 and N <= 1000:
            seed1 = self.df_seeds.iloc[N,0]
            seed2 = self.df_seeds.iloc[N,1]
        else:
            seed1 = 1
            seed2 = 1
        return seed1, seed2
        

        

