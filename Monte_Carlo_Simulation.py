from numpy import printoptions
from MC.random_number_generator import RandomGenerator
from MC.distribution_samplings import RandomSampling

def example_function(x):
    return x**2

rg = RandomGenerator()
sampling = RandomSampling()

seed1, seed2 = rg.random_seed(5)
random_number = rg.generate_random_number(seed1, seed2)

print(f"The seeds are:{seed1} y {seed2}")
print(f'The random value is: {random_number}')

### Integral - MC

total = 0
n = 100000
a = 0
b = 1
for _ in range(n):
    seed1, seed2 = rg.random_seed(5)
    random_number = rg.generate_random_number(seed1, seed2)
    x = sampling.uniform(random_number, a, b)
    total += example_function(x)

Integral_value = (b - a) * (total / n)
print(f'The integral value:{Integral_value}')