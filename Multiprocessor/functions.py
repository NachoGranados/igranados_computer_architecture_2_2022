# libraries
from math import *
from random import *
from constants import *

"""
This function calculates the binomial distribution based on
n number of trials, x number of successes and p probability
of getting a success
"""
def binomialDistribution(n, x, p):
    
	aux = (factorial(n)) / (factorial(n - x) * factorial(x))

	probability = aux * pow(p, x) * pow(1 - p, n - x)

	return probability

# generate random value for binomial distribution
n = randint(RANDOM_MIN, RANDOM_MAX)
x = n
p = random()

# check that x is less than n
while(x >= n):
	x = randint(RANDOM_MIN, RANDOM_MAX)

# calculate probability in percentage
probability = binomialDistribution(n, x, p) * 100

print("n = ", n)
print("p = ", p)
print("x = ", x)
print("binomial = ", probability)
