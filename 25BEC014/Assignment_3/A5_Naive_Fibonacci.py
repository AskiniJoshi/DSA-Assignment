"""
Assignment 3 - Part A: Recursion
Question A5 & A6: Naive Recursive Fibonacci, Call Tree, & Exponential Complexity Analysis
"""

call_counter = {}

def fib_counted(n, depth=0, log_tree=False):
    """
    Naive recursive Fibonacci that counts function invocations and
    optionally prints a text representation of the call tree.
    """
    call_counter[n] = call_counter.get(n, 0) + 1

    indent = "  " * depth
    if log_tree:
        print(f"{indent}fib({n})")

    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Naive recursive subproblem calls
    return fib_counted(n - 1, depth + 1, log_tree) + fib_counted(n - 2, depth + 1, log_tree)


def print_fib5_tree():
    """
    Visual ASCII depiction of the complete recursion tree for fib(5).
    """
    print("""

RECURSION TREE FOR fib(5) (Part A - Question 5)


                                fib(5)
                              /        \\
                    fib(4)                  fib(3)
                   /      \\                /      \\
             fib(3)        fib(2)        fib(2)    fib(1)
            /      \\      /      \\      /      \\
        fib(2)   fib(1) fib(1) fib(0) fib(1) fib(0)
       /      \\
    fib(1)   fib(0)


IDENTIFICATION OF REDUNDANT / REPEATED SUBPROBLEMS:

- fib(3) is called 2 separate times (entire subtree evaluated twice!)
- fib(2) is called 3 separate times (entire subtree evaluated 3 times!)
- fib(1) is called 5 separate times
- fib(0) is called 3 separate times
- TOTAL CALLS to compute fib(5) = 15 calls for an output of only 5!
""")


def analyze_exponential_growth():
    print("=" * 65)
    print("ANALYSIS OF CALLS MADE BY NAIVE FIBONACCI (Question A6)")
    print("=" * 65)
    print(f"{'n':<6} {'fib(n)':<10} {'Total Recursive Calls':<25} {'2^n Upper Bound'}")
    print("-" * 65)

    for n in range(1, 16):
        call_counter.clear()
        val = fib_counted(n, log_tree=False)
        total_calls = sum(call_counter.values())
        upper_bound = 2 ** n
        print(f"{n:<6} {val:<10} {total_calls:<25} {upper_bound}")

    print("-" * 65)
    print("""
Why Running Time Grows Exponentially:
1. Recurrence Relation for Number of Calls:
      T(0) = 1,  T(1) = 1
      T(n) = T(n - 1) + T(n - 2) + 1  for n >= 2
2. By induction, T(n) = 2 * F(n+1) - 1, where F(k) is the k-th Fibonacci number.
3. The closed form (Binet's formula) reveals:
      F(n) = (phi^n - psi^n) / sqrt(5)  where phi = (1 + sqrt(5))/2 ≈ 1.618
4. Thus, T(n) = Theta(phi^n) ≈ Theta(1.618^n) = O(2^n).
5. The branching factor of 2 at each internal node combined with massive
   subproblem overlap forces an exponential number of redundant calculations.
""")


if __name__ == "__main__":
    print_fib5_tree()

    print("\nExecuting live instrumented call for fib(5):")
    print("-" * 50)
    call_counter.clear()
    result = fib_counted(5, log_tree=True)
    print("-" * 50)
    print(f"fib(5) result: {result}")
    print("Breakdown of subproblem calls:")
    for k in sorted(call_counter.keys(), reverse=True):
        print(f"  fib({k}) called: {call_counter[k]} times")
    print()

    analyze_exponential_growth()
