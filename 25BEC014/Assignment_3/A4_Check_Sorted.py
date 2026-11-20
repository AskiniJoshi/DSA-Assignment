"""
Assignment 3 - Part A: Recursion
Question A4: Recursive Check for Non-Decreasing Order
"""

def is_sorted(S, index=0):
    """
    Recursively checks if sequence S is sorted in non-decreasing order.
    Returns True if sorted, False otherwise.
    """
    # Base case: 0 or 1 element, or reached the last element
    if len(S) <= 1 or index >= len(S) - 1:
        return True

    # Check current adjacent pair
    if S[index] > S[index + 1]:
        return False

    # Recursive call for remaining sequence
    return is_sorted(S, index + 1)


if __name__ == "__main__":
    print("=" * 65)
    print("RECURSIVE SORTED CHECK (Part A - Question 4)")
    print("=" * 65)

    test_cases = [
        ("Strictly increasing", [1, 2, 3, 4, 5], True),
        ("Non-decreasing with duplicates", [1, 2, 2, 4, 4, 5], True),
        ("Unsorted at beginning (Best Case O(1))", [10, 2, 3, 4, 5], False),
        ("Unsorted at end (Worst Case O(n))", [1, 2, 3, 4, 0], False),
        ("All identical elements", [7, 7, 7, 7], True),
        ("Single element", [42], True),
        ("Empty sequence", [], True)
    ]

    for desc, seq, expected in test_cases:
        res = is_sorted(seq)
        status = "PASS" if res == expected else "FAIL"
        print(f"[{status}] {desc:<38}: is_sorted({seq}) = {res}")

    print("\nComplexity Analysis:")
    print("  * Best-Case Time:  O(1) - immediate mismatch at index 0.")
    print("  * Worst-Case Time: O(n) - fully sorted sequence requires n-1 comparisons.")
    print("  * Auxiliary Space: O(n) - recursion call stack depth.")
