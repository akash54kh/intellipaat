import math


def prime_factors(n):
    factors = []

    # Extract all the factors of 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check odd numbers from 3 up to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # If n is still greater than 2, then n itself is prime
    if n > 2:
        factors.append(n)

    return factors


# Example usage:
num1 = 46
num2 = 78
print(f"Prime factors of {num1}: {prime_factors(num1)}")
print(f"Prime factors of {num2}: {prime_factors(num2)}")

