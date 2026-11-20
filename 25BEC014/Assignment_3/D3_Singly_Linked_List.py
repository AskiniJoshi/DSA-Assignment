"""
Assignment 3 - Part D: Linked Lists
Question D3: Singly Linked List: insert_first, insert_last, delete_first & Traversal

Node Structure:
    - _element: The data value stored at this node.
    - _next: Reference (pointer) to the subsequent node in the chain (or None).

Algorithms, Preconditions & Pointer Updates:
--------------------------------------------------------------------------------------
Operation      Precondition        Pointer Updates & Steps
--------------------------------------------------------------------------------------
insert_first   None                1. newest = Node(e, self._head)
                                   2. self._head = newest
                                   3. If self.is_empty(): self._tail = newest
                                   4. self._size += 1

insert_last    None                1. newest = Node(e, None)
                                   2. If self.is_empty(): self._head = newest
                                      Else: self._tail._next = newest
                                   3. self._tail = newest
                                   4. self._size += 1

delete_first   Not empty           1. If self.is_empty(): raise Empty
                                   2. answer = self._head._element
                                   3. self._head = self._head._next
                                   4. self._size -= 1
                                   5. If self.is_empty(): self._tail = None
                                   6. Return answer

traversal      None                1. current = self._head
                                   2. While current is not None:
                                        process current._element
                                        current = current._next
"""

class Empty(Exception):
    """Error accessing element from empty container."""
    pass


class SinglyLinkedList:
    """A lightweight singly linked list implementation."""

    class _Node:
        """Lightweight non-public structure for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next_node):
            self._element = element
            self._next = next_node

    def __init__(self):
        """Create an empty linked list."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insert_first(self, e):
        """Add an element e to the head of the list in O(1) time."""
        newest = self._Node(e, self._head)
        self._head = newest
        if self.is_empty():
            self._tail = newest  # Special case: previously empty
        self._size += 1

    def insert_last(self, e):
        """Add an element e to the tail of the list in O(1) time."""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest  # Special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def delete_first(self):
        """
        Remove and return the first element in O(1) time.
        Raises Empty exception if list is empty.
        """
        if self.is_empty():
            raise Empty("List is empty: cannot delete from head.")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None  # Special case: list became empty
        return answer

    def traverse(self):
        """Traverse the linked list and return elements as a Python list in O(n) time."""
        elements = []
        curr = self._head
        while curr is not None:
            elements.append(curr._element)
            curr = curr._next
        return elements

    def __repr__(self):
        nodes = [str(x) for x in self.traverse()]
        return f"[{' -> '.join(nodes) if nodes else 'EMPTY'}] (size={self._size})"


if __name__ == "__main__":
    print("=" * 70)
    print("TESTING SINGLY LINKED LIST (Part D - Question 3)")
    print("=" * 70)

    sll = SinglyLinkedList()
    print(f"Initial State: {sll}")
    print(f"is_empty: {sll.is_empty()} | size: {len(sll)}")
    print("-" * 55)

    # 1. Test insert_first
    print("Action: insert_first(20), insert_first(10)")
    sll.insert_first(20)
    sll.insert_first(10)
    print(f"Current List: {sll}")
    print("-" * 55)

    # 2. Test insert_last
    print("Action: insert_last(30), insert_last(40)")
    sll.insert_last(30)
    sll.insert_last(40)
    print(f"Current List: {sll}")
    print("-" * 55)

    # 3. Test traversal
    print("Action: Traversal of elements:")
    for idx, val in enumerate(sll.traverse()):
        print(f"  Node #{idx}: element = {val}")
    print("-" * 55)

    # 4. Test delete_first
    print(f"delete_first() returned: {sll.delete_first()}")
    print(f"Current List: {sll}")
    print(f"delete_first() returned: {sll.delete_first()}")
    print(f"Current List: {sll}")
    print("-" * 55)

    # 5. Empty the list
    print(f"delete_first() returned: {sll.delete_first()}")
    print(f"delete_first() returned: {sll.delete_first()}")
    print(f"Current List after clearing: {sll}")
    print(f"is_empty? {sll.is_empty()}")

    # 6. Test exception on empty deletion
    try:
        sll.delete_first()
    except Empty as e:
        print(f"Caught expected Empty exception: '{e}'")
