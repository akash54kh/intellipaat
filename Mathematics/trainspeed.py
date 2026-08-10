import random, math

s1 = s2 = 1

while math.gcd(s1, s2) == 1:
    s1 = random.randint(70, 100)
    s2 = random.randint(70, 100)

if s1 > s2:
    temp = s2
    s2 = s1
    s1 = temp

d = math.lcm(s1, s2)
s = s2 - s1

t1 = d / s1
t2 = (s1 * t1) / s2
t = int(t1 - t2)
c = s1 * s2

print('Distance: {}, Speed Increment: {}, Time Variation: {}'.format(d, s, t))
print('Actual Answer: {}km/hr, Negative Answer: {}km/hr'.format(s1, s2))
print('A = 1, B = {}, C = -{}'.format(s, c))

print("A train travels {} km. If speed increases by {} kmph, the journey takes {} hours less. Find the original speed!".format(d, s, t))

