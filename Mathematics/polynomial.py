import random
import numpy as np

degree = [3]
My_type = random.choice(degree)

random_x = random.randint(-10, 10)

if My_type == 1:
    A = random.randint(2, 5)
    B = random.randint(2, 10)
    symbol = random.choice(["+", "-"])
    print('Polynomial: {}x {} {}'.format(A, symbol, B))

    if symbol == "+":
        val = A*random_x + B
    else:
        val = A*random_x - B
    print('p(', random_x, ') = ', val)

if My_type == 2:
    A = random.randint(2, 5)
    B = random.randint(2, 10)
    C = random.randint(2, 50)
    symbol1 = random.choice(["+", "-"])
    symbol2 = random.choice(["+", "-"])
    print('Polynomial: {}(x2) {} {}x {} {}'.format(A, symbol1, B, symbol2, C))

    if symbol1 == '+' and symbol2 == '-':
        val = A * random_x * random_x + B * random_x - C
    elif symbol1 == '-' and symbol2 == '+':
        val = A * random_x * random_x - B * random_x + C
    elif symbol1 == '+' and symbol2 == '+':
        val = A * random_x * random_x + B * random_x + C
    else:
        val = A * random_x * random_x - B * random_x - C
    print('p(', random_x, ') = ', val)

if My_type == 3:
    A = random.randint(2, 5)
    B = random.randint(2, 10)
    C = random.randint(2, 54)
    D = random.randint(2, 50)
    option = random.choice([1, 2, 3])
    if option == 1:
        B, C = 0, 0
        symbol = random.choice(["+", "-"])
        print('Polynomial: {}(x3) {} {}'.format(A, symbol, D))

        if symbol == "+":
            val = A * random_x * random_x * random_x + D
        else:
            val = A * random_x * random_x * random_x - D
        print('p(', random_x, ') = ', val)

    elif option == 2:
        symbol1 = random.choice(["+", "-"])
        symbol2 = random.choice(["+", "-"])
        print('Polynomial: {}(x3) {} {}x {} {}'.format(A, symbol1, C, symbol2, D))

        if symbol1 == '+' and symbol2 == '-':
            val = A * random_x * random_x * random_x + C * random_x - D
        elif symbol1 == '-' and symbol2 == '+':
            val = A * random_x * random_x * random_x - C * random_x + D
        elif symbol1 == '+' and symbol2 == '+':
            val = A * random_x * random_x * random_x + C * random_x + D
        else:
            val = A * random_x * random_x * random_x - C * random_x - D
        print('p(', random_x, ') = ', val)

    else:
        symbol1 = random.choice(["+", "-"])
        symbol2 = random.choice(["+", "-"])
        symbol3 = random.choice(["+", "-"])
        print('Polynomial: {}(x3) {} {}(x2) {} {}x {} {}'.format(A, symbol1, B, symbol2, C, symbol3, D))

        if symbol1 == '-':
            B = -B
        if symbol2 == '-':
            C = -C
        if symbol3 == '-':
            D = -D

        coeffs = [A, B, C, D]
        #print(coeffs)
        x_point = random_x
        val = np.polyval(coeffs, x_point)
        val = int(val)
        print('p(', random_x, ') = ', val)




