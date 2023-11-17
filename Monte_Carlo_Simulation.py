import numpy as np
from MC.random_number_generator import RandomGenerator
from MC.distribution_samplings import RandomSampling

def example_function(x):
    return x**2

rg = RandomGenerator()
sampling = RandomSampling()

### Integral - MC Penelope
total = 0
n = 1000000
a = 0
b = 1
seed1, seed2 = rg.random_seed(5)

for _ in range(n):
    random_number, seed1, seed2, = rg.generate_random_number(seed1, seed2)
    x = sampling.uniform(random_number, a, b)
    total += example_function(x)

Integral_value = (b - a) * (total / n)
print(f'The integral Penelope value is : {Integral_value}')

## Integral - MC Numpy

np.random.seed(5)  
random_numbers = np.random.rand(10000)   

a = 0
b = 1

x_values = sampling.uniform(random_numbers, a, b)
total = np.sum(example_function(x_values))

integral_value = (b - a) * (total / 10000)
print(f'The integral Numpy value: {integral_value}')