"""
Assignment 3 - Part A: Recursion
Question A9: Converting Tail-Recursive Algorithm to Iterative & Stack Comparison
"""

def tail_recursive_sum(S, index=0, accumulator=0):
    """
    Tail-recursive sequence summation.
    Notice the recursive call is returned directly with an updated accumulator.
    """
    # Base case: reached the end of the sequence
    if index >= len(S):
        return accumulator
    # Tail-recursive call
    return tail_recursive_sum(S, index + 1, accumulator + S[index])


def iterative_sum(S):
    """
    Iterative conversion of the tail-recursive algorithm.
    The accumulator becomes a local variable, and the recursive call becomes a loop.
    """
    accumulator = 0
    index = 0
    n = len(S)
    while index < n:
        accumulator += S[index]
        index += 1
    return accumulator


def tail_recursive_binary_search(arr, target, low, high):
    """Tail-recursive binary search."""
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return tail_recursive_binary_search(arr, target, mid + 1, high)
    else:
        return tail_recursive_binary_search(arr, target, low, mid - 1)


def iterative_binary_search(arr, target):
    """Iterative conversion of tail-recursive binary search."""
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    print("=" * 68)
    print("TAIL-RECURSIVE TO ITERATIVE CONVERSION (Part A - Question 9)")
    print("=" * 68)

    sample_seq = [12, 25, 8, 33, 47, 19, 5]
    print(f"Test Sequence: {sample_seq}")

    sum_rec = tail_recursive_sum(sample_seq)
    sum_iter = iterative_sum(sample_seq)

    print(f"Tail-Recursive Sum Result: {sum_rec}")
    print(f"Iterative Sum Result:      {sum_iter}")
    print(f"Outputs match:             {sum_rec == sum_iter}\n")

    sorted_arr = [10, 20, 30, 40, 50, 60, 70, 80]
    target = 50
    bs_rec = tail_recursive_binary_search(sorted_arr, target, 0, len(sorted_arr) - 1)
    bs_iter = iterative_binary_search(sorted_arr, target)
    print(f"Binary Search for {target} in {sorted_arr}:")
    print(f"Tail-Recursive Index:      {bs_rec}")
    print(f"Iterative Index:           {bs_iter}")
    print(f"Outputs match:             {bs_rec == bs_iter}\n")

    print("=" * 68)
    print("CALL-STACK SPACE COMPARISON:")
    print("=" * 68)
    print("""
1. Tail-Recursive Version:
   - Call Stack Space: O(n) activation frames (in Python).
   - Python's standard CPython runtime does NOT optimize tail calls (no TCO).
   - Each call pushes a new frame storing parameters (index, accumulator) and
     return addresses, risking 'RecursionError: maximum recursion depth exceeded'
     when n > 1000.

2. Iterative Version:
   - Call Stack Space: O(1) auxiliary space.
   - Only a single stack frame is used for the entire function execution.
   - State updates occur by mutating local variables inside CPU registers or
     the current frame without creating any new activation records.
   - Can easily handle sequences of millions of elements without stack overflow.
""")
