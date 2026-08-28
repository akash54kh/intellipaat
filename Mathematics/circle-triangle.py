import random
import math

def generate_valid_triangle(min_val=1, max_val=8):
    """Generates three random side lengths that form a valid triangle."""
    max_val2 = max_val + 10
    min_val2 = min_val + 5
    while True:
        # 1. Generate three random integers within your desired range
        a = random.randint(min_val, max_val)
        b = random.randint(min_val2, max_val2)
        c = random.randint(min_val, max_val)

        # 2. Enforce the triangle inequality theorem
        if (a + b > c) and (a + c > b) and (b + c > a):
            return a, b, c


# Example usage
a, b, c = generate_valid_triangle()
print(f"Valid Triangle Sides: a={a}, b={b}, c={c}")


def get_incircle_radius(a, b, c):
    # Check if the sides can form a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given sides do not form a valid triangle.")

    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Calculate the radius of the incircle
    r = area / s
    return r

print('Radius shall be <{}>'.format(get_incircle_radius(a, b, c)))
