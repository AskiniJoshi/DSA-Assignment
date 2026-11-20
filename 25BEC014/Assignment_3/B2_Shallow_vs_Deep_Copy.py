"""
Assignment 3 - Part B: Array-Based Sequences
Question B2: Shallow Copy vs Deep Copy with Nested Lists
"""

import copy

def demonstrate_copies():
    print("=" * 70)
    print("SHALLOW COPY vs DEEP COPY DEMONSTRATION (Part B - Question 2)")
    print("=" * 70)

    # Original nested list: outer list containing two inner lists
    original = [[1, 2, 3], [4, 5, 6]]

    # Create shallow copy and deep copy
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)

    print("Initial State:")
    print(f"  original:  {original} (id outer: {id(original)}, id inner[0]: {id(original[0])})")
    print(f"  shallow:   {shallow} (id outer: {id(shallow)}, id inner[0]: {id(shallow[0])})")
    print(f"  deep:      {deep} (id outer: {id(deep)}, id inner[0]: {id(deep[0])})")
    print("-" * 70)

    # Explanation of IDs:
    print("\nMemory ID Analysis:")
    print(f"  Are outer IDs different? original vs shallow: {id(original) != id(shallow)} (True)")
    print(f"  Are inner IDs the SAME?   original[0] vs shallow[0]: {id(original[0]) == id(shallow[0])} (SHARED!)")
    print(f"  Are inner IDs DIFFERENT? original[0] vs deep[0]:    {id(original[0]) != id(deep[0])} (INDEPENDENT!)")
    print("-" * 70)

    # MUTATION 1: Modifying an inner mutable object in original
    print("\nAction 1: Modifying inner element: original[0][0] = 999")
    original[0][0] = 999
    print(f"  original:  {original}")
    print(f"  shallow:   {shallow}  <-- AFFECTED! (because original[0] and shallow[0] point to same list)")
    print(f"  deep:      {deep}  <-- UNAFFECTED! (holds independent clone)")
    print("-" * 70)

    # MUTATION 2: Appending to the outer list of shallow copy
    print("\nAction 2: Appending to outer container: shallow.append([7, 8])")
    shallow.append([7, 8])
    print(f"  original:  {original}  <-- UNAFFECTED! (outer lists are distinct)")
    print(f"  shallow:   {shallow}")
    print(f"  deep:      {deep}  <-- UNAFFECTED!")
    print("-" * 70)

    # MUTATION 3: Modifying deep copy inner list
    print("\nAction 3: Modifying deep copy inner element: deep[1][2] = -42")
    deep[1][2] = -42
    print(f"  original:  {original}  <-- UNAFFECTED!")
    print(f"  shallow:   {shallow}  <-- UNAFFECTED!")
    print(f"  deep:      {deep}")
    print("=" * 70)


if __name__ == "__main__":
    demonstrate_copies()
