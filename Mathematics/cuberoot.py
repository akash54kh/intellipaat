import math
import random

cube_tuple = tuple(i**3 for i in range(1, 201))

# 1. Generate a random integer between 1 and 1000
random_number = random.choice(cube_tuple)

# 2. Calculate the cube root
cube_root = math.cbrt(random_number)
cube_root = int(cube_root)

# 3. Print the results
print(f"Random Number: {random_number}")
print(f"Cube Root: {cube_root}")
