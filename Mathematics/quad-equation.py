import random, math
from fractions import Fraction

option = random.choice([True, False])

if option:
    alpha = random.randint(-50, 50)
    beta = random.randint(-50, 50)

    while alpha == beta or alpha == 0 or beta == 0:
        alpha = random.randint(-50, 50)
        beta = random.randint(1, 50)

    A = 1
    B = -(alpha + beta)
    C = alpha * beta

    print('Quad Equation: A = {}, B = {}, C = {}'.format(A, B, C))
    print('The zeros are: {} and {}'.format(alpha, beta))

else:
    option = random.choice([True, False])

    if option:
        r1 = Fraction(random.randint(-10, 10), random.randint(-10, 10))
        r2 = Fraction(random.randint(-10, 10), random.randint(-10, 10))
    else:
        r1 = random.randint(-40, 50)
        r2 = Fraction(random.randint(-10, 10), random.randint(-10, 10))

    alpha = r1 + r2
    beta = r1 * r2

    A = int(alpha.denominator * beta.denominator)
    B = -int(alpha * A)
    C = int(beta * A)

    current_hcf = math.gcd(A, B, C)

    reduced_a = A // current_hcf
    reduced_b = B // current_hcf
    reduced_c = C // current_hcf

    print('Quad Equation: A = {}, B = {}, C = {}'.format(reduced_a, reduced_b, reduced_c))
    print('The zeros are: {} and {}'.format(r1, r2))


