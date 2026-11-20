"""
Assignment 3 - Part C: Stacks, Queues and Deques
Question C8: Circular-Array Queue Implementation

Queue ADT (FIFO - First-In, First-Out):
    - enqueue(e): Add element e to the back of the queue.
    - dequeue(): Remove and return the front element of the queue.
    - first(): Return front element without removing it.
    - is_empty(): True if empty.
    - len(queue): Number of stored elements.

Index Formulas Derived:
    Let:
        N = capacity of the underlying array self._data (i.e. len(self._data))
        _front = index of the current front element in self._data
        _size = number of elements currently stored in the queue
    
    1. Next Available Insertion Index (where enqueue places element e):
           avail = (_front + _size) % N
    
    2. Next Front Index (after dequeue removes the front element):
           new_front = (_front + 1) % N

Why Circular?
    In a linear array queue, dequeuing from index 0 wastes space on the left
    or forces an O(n) shift of all subsequent elements. Using modular arithmetic
    allows the queue to wrap around the end of the array to the front in O(1) time.
"""

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class ArrayQueue:
    """FIFO queue implementation using a circular Python list as underlying storage."""
    DEFAULT_CAPACITY = 10

    def __init__(self, capacity=None):
        """Create an empty queue with specified or default initial capacity."""
        cap = capacity if capacity is not None else self.DEFAULT_CAPACITY
        self._data = [None] * cap
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """
        Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty: cannot access front element.")
        return self._data[self._front]

    def dequeue(self):
        """
        Remove and return the first element of the queue (FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty: cannot dequeue.")
        answer = self._data[self._front]
        self._data[self._front] = None  # Assist garbage collection
        # Advance front pointer using circular modulo arithmetic
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of the queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # Double array size if full
        # Compute circular insertion index
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """Resize internal storage to a new capacity >= len(self)."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def __repr__(self):
        """Show internal buffer and active window."""
        items = []
        walk = self._front
        for _ in range(self._size):
            items.append(str(self._data[walk]))
            walk = (walk + 1) % len(self._data)
        return f"Queue([{' -> '.join(items)}]) [Front={self._front}, Size={self._size}, Cap={len(self._data)}]"


if __name__ == "__main__":
    print("=" * 70)
    print("TESTING CIRCULAR-ARRAY QUEUE (Part C - Question 8)")
    print("=" * 70)

    # Initialize queue with small initial capacity (5) to test wrap-around & resizing
    Q = ArrayQueue(capacity=5)
    print(f"Created queue with initial capacity 5: {Q}")
    print(f"is_empty? {Q.is_empty()}")
    print("-" * 55)

    # 1. Enqueue 4 items
    print("Enqueuing: 10, 20, 30, 40")
    for x in [10, 20, 30, 40]:
        Q.enqueue(x)
    print(f"Queue state: {Q}")
    print(f"Front element: {Q.first()} | len: {len(Q)}")
    print("-" * 55)

    # 2. Dequeue 2 items (frees slots at index 0 and 1)
    print(f"Dequeued: {Q.dequeue()}")
    print(f"Dequeued: {Q.dequeue()}")
    print(f"Queue state after 2 dequeues: {Q}")
    print("-" * 55)

    # 3. Enqueue 3 items (demonstrating modular circular wrap-around!)
    print("Enqueuing: 50, 60, 70 (triggering wrap-around to index 0, 1...)")
    for x in [50, 60, 70]:
        Q.enqueue(x)
    print(f"Queue state after wrap-around: {Q}")
    print(f"Internal raw buffer: {Q._data}")
    print("-" * 55)

    # 4. Enqueue more to trigger dynamic resize
    print("Enqueuing: 80, 90 (triggers dynamic buffer resize to double capacity)")
    Q.enqueue(80)
    Q.enqueue(90)
    print(f"Queue state after resize: {Q}")
    print(f"Internal raw buffer: {Q._data}")
    print("-" * 55)

    # 5. Empty the queue
    print("Emptying queue:")
    while not Q.is_empty():
        print(f"  Dequeued: {Q.dequeue()}")

    # 6. Test exception on empty dequeue
    print("\nTesting exception handling on empty queue:")
    try:
        Q.dequeue()
    except Empty as e:
        print(f"  Caught expected Empty exception: '{e}'")
