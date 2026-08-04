import random, math

s1 = 1
s2 = 1

my_primes = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

while math.gcd(s1, s2) == 1 or s1 in my_primes and s2 in my_primes:
    s1 = random.randint(10, 100)
    s2 = random.randint(10, 100)

b = math.lcm(s1, s2)
a = math.gcd(s1, s2)

print('Find HCF and LCM of {} and {}.'.format(s1, s2))
print('HCF = {} and LCM = {}'.format(a, b))
