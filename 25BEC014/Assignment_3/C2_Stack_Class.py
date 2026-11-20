"""
Assignment 3 - Part C: Stacks, Queues and Deques
Question C2: Stack Class Implementation using Python List

ADT Specification:
    A stack is a Last-In, First-Out (LIFO) linear data structure.
    Methods:
        push(e):     Add element e to the top of the stack.
        pop():       Remove and return the top element from the stack;
                     raises Empty exception if the stack is empty.
        top():       Return a reference to the top element without removing it;
                     raises Empty exception if the stack is empty.
        is_empty():  Return True if the stack contains no elements, False otherwise.
        len(stack):  Return the number of elements in the stack.
"""

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty: cannot inspect top element.")
        return self._data[-1]

    def pop(self):
        """
        Remove and return the element from the top of the stack (LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty: cannot pop element.")
        return self._data.pop()

    def __repr__(self):
        """Return string representation of the stack."""
        return f"Stack({self._data})"


if __name__ == "__main__":
    print("=" * 65)
    print("TESTING ARRAY STACK IMPLEMENTATION (Part C - Question 2)")
    print("=" * 65)

    S = ArrayStack()
    print(f"Newly created stack: {S}")
    print(f"is_empty()? {S.is_empty()} | len: {len(S)}")
    print("-" * 50)

    # 1. Pushing elements
    print("Pushing elements: 5, 10, 15, 20")
    S.push(5)
    S.push(10)
    S.push(15)
    S.push(20)
    print(f"Current Stack: {S}")
    print(f"Top element: {S.top()} | len: {len(S)}")
    print("-" * 50)

    # 2. Popping elements
    print(f"Popped: {S.pop()}")
    print(f"Popped: {S.pop()}")
    print(f"Current Stack: {S}")
    print(f"Top element: {S.top()}")
    print("-" * 50)

    # 3. Pushing more elements
    print("Pushing 99")
    S.push(99)
    print(f"Current Stack: {S}")
    print("-" * 50)

    # 4. Emptying the stack
    while not S.is_empty():
        print(f"Popped: {S.pop()}, remaining size: {len(S)}")

    print(f"Stack is now empty? {S.is_empty()}")
    print("-" * 50)

    # 5. Testing Exception Handling on Empty Stack
    print("Testing exception on empty stack:")
    try:
        S.pop()
    except Empty as e:
        print(f"  Caught expected exception on S.pop(): '{e}'")

    try:
        S.top()
    except Empty as e:
        print(f"  Caught expected exception on S.top(): '{e}'")

    print("\nAll Stack operations verified successfully!")
