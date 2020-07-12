

#   Finds the largest prime factor for a given number
#   Gets the factors of a number
import math

largestPrimefactor = 0

def FactorFinder(number):

    Factors = []
#   Factors of n are all numbers that divide into n evenly 
#   Improvement: Upper limit is set at the square root of n 

#                If one factor is bigger, the other factor is smaller
#                This means that one of the two will always <= sqrt(number)

    for i in range(1, int(math.sqrt(number)+1)):
        if number % i == 0:
            Factors.append(i)
            Factors.append(number // i)
    return Factors

#   Checks if the factor is prime 
#   A prime can only be divided evenly by 1 and itself

def IsPrime(number):
    
#   If number is prime, it should only return 2 roots

    return len(FactorFinder(number)) == 2

allFactors = FactorFinder(600851475143)

for factor in allFactors:
    if IsPrime(factor) and factor > largestPrimefactor:
        largestPrimefactor = factor
print(largestPrimefactor)
    





