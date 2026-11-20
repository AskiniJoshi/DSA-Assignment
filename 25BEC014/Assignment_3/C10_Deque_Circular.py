"""
Assignment 3 - Part C: Stacks, Queues and Deques
Question C10: Double-Ended Queue (Deque) using Circular-Array Indexing

Deque ADT (Double-Ended Queue):
    Supports insertions and deletions at both front and back in O(1) time.

Circular-Array Indexing Formulas:
    Let:
        N = len(self._data) (capacity)
        _front = index of front element
        _size = number of elements stored

    1. add_first(e):
       New front position decrements circularly:
           self._front = (self._front - 1) % N
           self._data[self._front] = e

    2. add_last(e):
       Inserted at the next available back position:
           avail = (self._front + self._size) % N
           self._data[avail] = e

    3. delete_first():
       Element at _front is removed; front pointer increments circularly:
           val = self._data[self._front]
           self._front = (self._front + 1) % N

    4. delete_last():
       Element at the last active slot is removed:
           last_idx = (self._front + self._size - 1) % N
           val = self._data[last_idx]
"""

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class ArrayDeque:
    """Double-ended queue implementation using a circular array."""
    DEFAULT_CAPACITY = 8

    def __init__(self, capacity=None):
        cap = capacity if capacity is not None else self.DEFAULT_CAPACITY
        self._data = [None] * cap
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """Return (do not remove) the first element."""
        if self.is_empty():
            raise Empty("Deque is empty.")
        return self._data[self._front]

    def last(self):
        """Return (do not remove) the last element."""
        if self.is_empty():
            raise Empty("Deque is empty.")
        last_idx = (self._front + self._size - 1) % len(self._data)
        return self._data[last_idx]

    def add_first(self, e):
        """Add element e to the front of the deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        # Circular decrement of front pointer
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        """Add element e to the back of the deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        # Circular position for the new back element
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def delete_first(self):
        """Remove and return the front element."""
        if self.is_empty():
            raise Empty("Deque is empty.")
        answer = self._data[self._front]
        self._data[self._front] = None  # GC
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def delete_last(self):
        """Remove and return the last element."""
        if self.is_empty():
            raise Empty("Deque is empty.")
        last_idx = (self._front + self._size - 1) % len(self._data)
        answer = self._data[last_idx]
        self._data[last_idx] = None  # GC
        self._size -= 1
        return answer

    def _resize(self, cap):
        """Resize circular buffer to new capacity."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def __repr__(self):
        items = []
        walk = self._front
        for _ in range(self._size):
            items.append(str(self._data[walk]))
            walk = (walk + 1) % len(self._data)
        return f"Deque([{', '.join(items)}]) (len={self._size}, cap={len(self._data)})"


if __name__ == "__main__":
    print("=" * 70)
    print("TESTING CIRCULAR ARRAY DEQUE (Part C - Question 10)")
    print("=" * 70)

    D = ArrayDeque(capacity=5)
    print(f"Created empty Deque: {D}")
    print("-" * 55)

    # 1. Add elements at both ends
    print("Action: add_last(10), add_last(20), add_first(5), add_first(1)")
    D.add_last(10)
    D.add_last(20)
    D.add_first(5)
    D.add_first(1)
    print(f"Deque state: {D}")
    print(f"First element: {D.first()}, Last element: {D.last()}")
    print("-" * 55)

    # 2. Delete from both ends
    print(f"delete_first() -> {D.delete_first()}")
    print(f"delete_last()  -> {D.delete_last()}")
    print(f"Deque state: {D}")
    print("-" * 55)

    # 3. Add more elements to trigger wrap-around and resizing
    print("Action: add_last(30), add_last(40), add_first(0)")
    D.add_last(30)
    D.add_last(40)
    D.add_first(0)
    print(f"Deque state: {D}")
    print(f"Internal storage buffer: {D._data}")
    print("-" * 55)

    # 4. Empty the deque from opposite sides
    print("Emptying deque (alternating ends):")
    print(f"  delete_first() -> {D.delete_first()}")
    print(f"  delete_last()  -> {D.delete_last()}")
    print(f"  delete_first() -> {D.delete_first()}")
    print(f"  delete_last()  -> {D.delete_last()}")
    print(f"  delete_first() -> {D.delete_first()}")
    print(f"Is deque empty? {D.is_empty()}")

    # 5. Exception handling
    try:
        D.delete_first()
    except Empty as e:
        print(f"Caught expected Empty exception: '{e}'")
