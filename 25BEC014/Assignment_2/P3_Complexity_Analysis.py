"""
Assignment 2 - Part 3: Step-by-Step Complexity Analysis of Python Algorithms

Objective:
    1. Loop that repeatedly replaces n by floor(n/2) until n <= 1.
       Derives and logs iteration count against floor(log2(n)).
    2. Comparison of prefix average implementations (Summary execution).
    3. Three element-uniqueness algorithms:
       - Method 1: Brute force (pairwise comparison) -> O(n^2) time, O(1) space.
       - Method 2: Sorting-based -> O(n log n) time, O(1) auxiliary space.
       - Method 3: Hash-set based -> O(n) expected time, O(n) auxiliary space.

Author: ASKINI JOSHI 25BEC014
"""

import math
import time
import random


# 1. LOOP HALVING ANALYSIS: n -> floor(n/2) until n <= 1

def count_halving_iterations(n):
    """
    Replaces n by floor(n/2) until n <= 1.
    Returns the total number of division iterations executed.
    """
    if n <= 1:
        return 0
    count = 0
    curr = n
    while curr > 1:
        curr = curr // 2
        count += 1
    return count


def demonstrate_loop_halving():
    print("=" * 70)
    print("PART 3 - PROBLEM 1: LOOP HALVING ANALYSIS: n = floor(n/2)")
    print("=" * 70)
    print(f"{'Input n':<12} {'Iterations k':<16} {'floor(log2(n))':<18} {'Match?'}")
    print("-" * 70)

    test_values = [1, 2, 3, 4, 7, 8, 15, 16, 31, 32, 64, 100, 1024, 1000000]
    for n in test_values:
        k = count_halving_iterations(n)
        expected = math.floor(math.log2(n)) if n > 0 else 0
        match = "YES" if k == expected else "NO"
        print(f"{n:<12} {k:<16} {expected:<18} {match}")

    print("-" * 70)
    print("""
Derivation:
    Let n_0 = n. After iteration k, n_k = floor(n / 2^k).
    The loop terminates when n_k <= 1, which requires:
        n / 2^k <= 1  ==>  2^k >= n  ==>  k >= log2(n)
    Thus, exactly k = floor(log2(n)) divisions occur.
    Time Complexity: T(n) = O(log n)
    Auxiliary Space: O(1)
""")


# 2. THREE ELEMENT-UNIQUENESS METHODS

def unique1_brute_force(arr):
    """
    Method 1: Brute Force Pairwise Comparison
    Time Complexity: O(n^2)
    Space Complexity: O(1) auxiliary
    """
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return False  # Duplicate found
    return True  # All unique


def unique2_sorting(arr):
    """
    Method 2: Sorting-Based Comparison
    Time Complexity: O(n log n)
    Space Complexity: O(n) or O(1) depending on whether original is copied
    """
    # Create sorted copy to preserve original sequence
    temp = sorted(arr)
    for i in range(len(temp) - 1):
        if temp[i] == temp[i + 1]:
            return False  # Duplicate found
    return True  # All unique


def unique3_set(arr):
    """
    Method 3: Hash-Set Based Lookup
    Time Complexity: O(n) average
    Space Complexity: O(n) auxiliary
    """
    seen = set()
    for x in arr:
        if x in seen:
            return False  # Duplicate found
        seen.add(x)
    return True  # All unique


def demonstrate_uniqueness():
    print("=" * 70)
    print("PART 3 - PROBLEM 3: THREE ELEMENT-UNIQUENESS METHODS")
    print("=" * 70)

    # 1. Correctness tests
    test_cases = [
        ("All unique", [1, 5, 9, 3, 7, 2, 8]),
        ("One duplicate", [1, 5, 9, 3, 5, 2, 8]),
        ("Empty list", []),
        ("Singleton", [100]),
        ("All duplicates", [4, 4, 4, 4]),
    ]

    print("Equivalence & Correctness Verification:")
    print("-" * 55)
    for desc, seq in test_cases:
        r1 = unique1_brute_force(seq)
        r2 = unique2_sorting(seq)
        r3 = unique3_set(seq)
        print(f"Test '{desc}':")
        print(f"   Input: {seq}")
        print(f"   Brute Force: {r1} | Sorting: {r2} | Set: {r3} | Match: {r1 == r2 == r3}")
    print()

    # 2. Performance benchmark
    print("Performance Benchmarking on Unique Lists (Worst-Case Search):")
    print("-" * 70)
    print(f"{'Input Size (n)':<16} {'Brute Force O(n^2)':<20} {'Sorting O(n log n)':<20} {'Set O(n)'}")
    print("-" * 70)

    sizes = [500, 1000, 2000, 4000]
    for n in sizes:
        # A list of distinct integers triggers the worst case (checks entire list)
        arr = list(range(n))

        # Time method 1
        start = time.perf_counter()
        unique1_brute_force(arr)
        t1 = time.perf_counter() - start

        # Time method 2
        start = time.perf_counter()
        unique2_sorting(arr)
        t2 = time.perf_counter() - start

        # Time method 3
        start = time.perf_counter()
        unique3_set(arr)
        t3 = time.perf_counter() - start

        print(f"{n:<16} {t1:<20.6f} {t2:<20.6f} {t3:<20.6f}")

    print("-" * 70)
    print("""
Comparison Summary:
------------------------------------------------------------------------------
Method                 Time Complexity     Space Complexity    Practical Trade-offs
------------------------------------------------------------------------------
1. Brute Force         O(n^2)              O(1)                Simplest; in-place; slow for n > 10^3
2. Sorting-Based       O(n log n)          O(n) or O(1) in-pl  Fast; requires ordered/sortable keys
3. Hash-Set Based      O(n) average        O(n)                Fastest; requires hashable elements
------------------------------------------------------------------------------
""")


if __name__ == "__main__":
    demonstrate_loop_halving()
    demonstrate_uniqueness()
