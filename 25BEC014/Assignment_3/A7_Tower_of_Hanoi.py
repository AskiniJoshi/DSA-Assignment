"""
Assignment 3 - Part A: Recursion
Question A7: Tower of Hanoi Problem for n Disks 
"""

move_count = 0

def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solves the Tower of Hanoi problem recursively for n disks.
    """
    global move_count

    # Base case: only 1 disk to move
    if n == 1:
        move_count += 1
        print(f"  Move #{move_count:02d}: Move disk 1 from [{source}] ---> [{target}]")
        return

    # Step 1: Move top (n-1) disks from source to auxiliary using target
    tower_of_hanoi(n - 1, source, auxiliary, target)

    # Step 2: Move disk n from source to target
    move_count += 1
    print(f"  Move #{move_count:02d}: Move disk {n} from [{source}] ---> [{target}]")

    # Step 3: Move (n-1) disks from auxiliary to target using source
    tower_of_hanoi(n - 1, auxiliary, target, source)


if __name__ == "__main__":
    print("=" * 65)
    print("TOWER OF HANOI RECURSIVE SOLUTION (Part A - Question 7)")
    print("=" * 65)

    # Demonstration for n = 3 disks
    n_disks = 3
    move_count = 0
    print(f"\nSolving for n = {n_disks} disks (Expected moves = 2^{n_disks} - 1 = {2**n_disks - 1}):")
    print("-" * 55)
    tower_of_hanoi(n_disks, source='A (Source)', target='C (Target)', auxiliary='B (Auxiliary)')
    print("-" * 55)
    print(f"Completed in {move_count} moves.\n")

    # Demonstration for n = 4 disks
    n_disks = 4
    move_count = 0
    print(f"Solving for n = {n_disks} disks (Expected moves = 2^{n_disks} - 1 = {2**n_disks - 1}):")
    print("-" * 55)
    tower_of_hanoi(n_disks, source='Peg A', target='Peg C', auxiliary='Peg B')
    print("-" * 55)
    print(f"Completed in {move_count} moves.")
