# Prime Number Checker
# This script checks whether a given number is prime using GCD logic.
# It prints intermediate values like square root, iteration variable, and GCD.

import math


def is_prime(num):
    """
    Check if the number is prime by verifying that GCD of any number
    in range [2, sqrt(num)] with the input number is 1.
    """
    sqrt = math.isqrt(num)
    print(f"Square root of {num} (rounded down): {sqrt}")

    for i in range(2, sqrt + 1):
        print(f"Checking with i = {i}")
        gcd = math.gcd(i, num)
        print(f"GCD of {i} and {num} = {gcd}")

        if gcd > 1:
            print(f"{num} is not a prime number.")
            return False

    print(f"{num} is a prime number.")
    return True


try:
    user_input = int(input("Enter a number to check if it's prime: "))
    is_prime(user_input)
except ValueError:
    print("Invalid input. Please enter an integer.")
