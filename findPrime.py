from math import sqrt

def is_prime(x):
    if x<2:
        return False
    for i in range (2, int(sqrt(x)+1)):
        if x%i == 0:
            return False
        return True

primes = [print("Heyyooo -1 ", x) for x in range(101) if is_prime(x)]
#[print("Heyyooo", x) for x in primes]
#for i in primes:
 #   print(i)
#print(primes)
