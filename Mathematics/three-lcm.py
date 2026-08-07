import random, math

s1, s2, s3 = 1, 1, 1

pr = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def boolean_value(s1, s2, s3):
    if s1 == s2 or s2 == s3 or s3 == s1 or s1 in pr and s2 in pr and s3 in pr:
        return True
    else:
        return False

while math.gcd(s1, s2, s3) == 1 or boolean_value(s1, s2, s3):
    s1 = random.randint(10, 100)
    s2 = random.randint(10, 100)
    s3 = random.randint(10, 100)

bell = math.lcm(s1, s2, s3)

print('Three numbers are {}, {} and {}'.format(s1, s2, s3))
print('LCM of three numbers: ', bell)
print('')
print('Three bells ring at intervals of {}, {} and {} minutes respectively. '
      'If they start ringing together, after what time will they next ring together?'
      .format(s1, s2, s3))
print('LCM of three numbers: ', bell)
