"""
Assignment 3 - Part A: Recursion
Question A2: Recursive Functions for Factorial, Sum of Natural Numbers, and Power
"""

def factorial(n):
    """Computes factorial of n recursively."""
    if n < 0:
        raise ValueError("Factorial is undefined for negative integers.")
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive step
    return n * factorial(n - 1)


def sum_natural(n):
    """Computes the sum of first n natural numbers (1 to n) recursively."""
    if n <= 0:
        raise ValueError("Sum of natural numbers requires n >= 1.")
    # Base case
    if n == 1:
        return 1
    # Recursive step
    return n + sum_natural(n - 1)


def power(x, n):
    """Computes x^n recursively using repeated multiplication."""
    if n < 0:
        raise ValueError("Power exponent n must be non-negative.")
    # Base case
    if n == 0:
        return 1
    # Recursive step
    return x * power(x, n - 1)


def power_optimized(x, n):
    """
    Optimized O(log n) recursive power using squaring:
    x^n = (x^(n/2))^2 if n is even, x * (x^(n/2))^2 if n is odd.
    """
    if n == 0:
        return 1
    partial = power_optimized(x, n // 2)
    result = partial * partial
    if n % 2 == 1:
        result *= x
    return result


if __name__ == "__main__":
    print("=" * 60)
    print("TESTING RECURSIVE FUNCTIONS (Part A - Question 2)")
    print("=" * 60)

    # 1. Factorial tests
    print("1. Factorial:")
    for num in [0, 1, 5, 7]:
        print(f"   factorial({num}) = {factorial(num)}")
    print()

    # 2. Sum of natural numbers tests
    print("2. Sum of First n Natural Numbers:")
    for num in [1, 5, 10, 100]:
        print(f"   sum_natural({num}) = {sum_natural(num)}")
    print()

    # 3. Power tests
    print("3. Power Computation (x^n):")
    test_cases = [(2, 0), (2, 5), (3, 4), (5, 3), (10, 4)]
    for x, n in test_cases:
        p_basic = power(x, n)
        p_opt = power_optimized(x, n)
        print(f"   power({x}, {n}) = {p_basic} (Optimized O(log n): {p_opt})")
    print()
    print("All recursive functions executed successfully!")
