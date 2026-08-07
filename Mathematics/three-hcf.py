import random, math

s1, s2, s3 = 1, 1, 1

pr = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def boolean_value(s1, s2, s3):
    if s1 == s2 or s2 == s3 or s3 == s1 or s1 in pr and s2 in pr and s3 in pr:
        return True
    elif math.gcd(s1, s2, s3) <= 6:
        return True
    else:
        return False

while math.gcd(s1, s2, s3) == 1 or boolean_value(s1, s2, s3):
    s1 = random.randint(300, 360)
    s2 = random.randint(220, 280)
    s3 = random.randint(80, 99)

stacks = math.gcd(s1, s2, s3)

print('Three sets of English, Hindi and Mathematics books containing {}, {} and {} books respectively have to be'
      ' stacked in such a way that all the books are stored topic-wise and the height of each stack is the same. '
      'Assuming that the books are of the same thickness, determine the number of stacks of English, '
      'Hindi and Mathematics books.'.format(s1, s2, s3))
print('Answer:', stacks)