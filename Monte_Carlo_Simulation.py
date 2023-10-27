from numpy import printoptions
from MC.random_number_generator import RandomGenerator

rg = RandomGenerator()
seed1, seed2 = rg.random_seed(5)

print(f"The seeds are:{seed1} y {seed2}")

random_number = rg.generate_random_number(seed1, seed2)

print(f'The random value is: {random_number}')