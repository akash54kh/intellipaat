import random

a = b = 1
while a == b or a > b:
    a = random.randint(1, 7)
    b = random.randint(1, 7)

x = random.randrange(10, 240, 10)
a1 = a * x
b1 = b * x
num = a1 + b1

print('Divide {} in {}:{} ratio.'.format(num, a, b))
print('Answer = {}:{}'.format(a1, b1))


