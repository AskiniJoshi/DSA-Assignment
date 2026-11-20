"""
Assignment 3 - Part A: Recursion
Question A3: Recursive In-Place Sequence Reversal
"""

def reverse_inplace(S, start, stop, trace=False, depth=0):
    """
    Recursively reverses sequence S in-place between start and stop (inclusive).
    """
    indent = "  " * depth
    if trace:
        print(f"{indent}-> Call: reverse(start={start}, stop={stop}), current state: {S}")

    # Base case: indices have met or crossed
    if start >= stop:
        if trace:
            print(f"{indent}* Base case reached (start >= stop). Terminating recursion.")
        return

    # Swap elements at endpoints
    S[start], S[stop] = S[stop], S[start]
    if trace:
        print(f"{indent}  Swapped S[{start}] <-> S[{stop}]: new state: {S}")

    # Recursive call on inner sub-sequence
    reverse_inplace(S, start + 1, stop - 1, trace=trace, depth=depth + 1)


if __name__ == "__main__":
    print("=" * 65)
    print("RECURSIVE IN-PLACE SEQUENCE REVERSAL (Part A - Question 3)")
    print("=" * 65)

    # 1. Trace for a sequence of six elements
    seq_six = [10, 20, 30, 40, 50, 60]
    print(f"Original Sequence (n=6): {seq_six}\n")
    print("Detailed Execution Trace:")
    print("-" * 50)
    reverse_inplace(seq_six, 0, len(seq_six) - 1, trace=True)
    print("-" * 50)
    print(f"Final Reversed Sequence: {seq_six}\n")

    # 2. Additional test with odd number of elements (5 elements)
    seq_odd = ['a', 'b', 'c', 'd', 'e']
    print(f"Testing Odd-Length Sequence: {seq_odd}")
    reverse_inplace(seq_odd, 0, len(seq_odd) - 1)
    print(f"Reversed: {seq_odd}\n")

    # 3. Edge cases
    empty = []
    reverse_inplace(empty, 0, len(empty) - 1)
    print(f"Empty sequence reversed: {empty}")

    single = [99]
    reverse_inplace(single, 0, len(single) - 1)
    print(f"Single-element sequence reversed: {single}")
