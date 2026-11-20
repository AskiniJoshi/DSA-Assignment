"""
Assignment 3 - Part D: Linked Lists
Question D4: Doubly Linked List Pointer Updates: Insert Between & Delete Node

Doubly Linked List Structure:
    Each node contains three fields:
        - _element: Data payload
        - _prev: Reference to the predecessor node
        - _next: Reference to the successor node

Use of Sentinel Header and Trailer Nodes:
    Dummy header and trailer nodes eliminate edge cases for insertions and deletions
    at the ends, ensuring every data node is strictly between two existing nodes.

Pointer Updates Required:

1. Inserting Node 'newest' BETWEEN Existing Nodes 'predecessor' and 'successor':
   Step a: newest = _Node(e, predecessor, successor)
           (Sets newest._prev = predecessor, newest._next = successor)
   Step b: predecessor._next = newest
   Step c: successor._prev = newest
   Step d: self._size += 1
   Time Complexity: O(1)

2. Deleting an Existing Node 'node' (between predecessor and successor):
   Step a: predecessor = node._prev
   Step b: successor = node._next
   Step c: predecessor._next = successor
   Step d: successor._prev = predecessor
   Step e: self._size -= 1
   Step f: element = node._element
   Step g: node._prev = node._next = node._element = None  # Deprecate node (GC)
   Step h: Return element
   Time Complexity: O(1)
"""

class Empty(Exception):
    pass


class DoublyLinkedList:
    """A base doubly linked list implementation using sentinel nodes."""

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev_node, next_node):
            self._element = element
            self._prev = prev_node
            self._next = next_node

    def __init__(self):
        """Create an empty doubly linked list with header and trailer sentinels."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """
        Insert element e between existing nodes predecessor and successor.
        Returns the newly created node.
        """
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """
        Delete non-sentinel node from the list and return its element.
        """
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        # Deprecate fields to aid garbage collection
        node._prev = node._next = node._element = None
        return element

    def insert_first(self, e):
        """Insert element at front."""
        return self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Insert element at back."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Remove and return front element."""
        if self.is_empty():
            raise Empty("List is empty.")
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove and return back element."""
        if self.is_empty():
            raise Empty("List is empty.")
        return self._delete_node(self._trailer._prev)

    def to_list(self):
        """Traverse forward from header to trailer and return elements."""
        result = []
        curr = self._header._next
        while curr is not self._trailer:
            result.append(curr._element)
            curr = curr._next
        return result

    def to_list_reverse(self):
        """Traverse backward from trailer to header."""
        result = []
        curr = self._trailer._prev
        while curr is not self._header:
            result.append(curr._element)
            curr = curr._prev
        return result

    def __repr__(self):
        items = [str(x) for x in self.to_list()]
        return f"[Header <-> {' <-> '.join(items) if items else 'None'} <-> Trailer] (size={self._size})"


if __name__ == "__main__":
    print("=" * 70)
    print("TESTING DOUBLY LINKED LIST (Part D - Question 4)")
    print("=" * 70)

    dll = DoublyLinkedList()
    print(f"Empty DLL: {dll}")
    print("-" * 55)

    # 1. Insert between tests
    print("Inserting at ends: 10, 20, 30, 40")
    dll.insert_first(20)
    dll.insert_first(10)
    dll.insert_last(30)
    node40 = dll.insert_last(40)
    print(f"Current DLL: {dll}")
    print(f"Forward traversal:  {dll.to_list()}")
    print(f"Backward traversal: {dll.to_list_reverse()}")
    print("-" * 55)

    # 2. Insert between two specific internal nodes (insert 25 between 20 and 30)
    print("Action: Explicit insert_between(25) between node 20 and node 30:")
    node20 = dll._header._next._next  # node with element 20
    node30 = node20._next             # node with element 30
    node25 = dll._insert_between(25, node20, node30)
    print(f"Current DLL after inserting 25: {dll}")
    print(f"Forward traversal: {dll.to_list()}")
    print("-" * 55)

    # 3. Explicit delete_node test (delete node 25)
    print("Action: Explicit delete_node(node25):")
    deleted_val = dll._delete_node(node25)
    print(f"Deleted value: {deleted_val}")
    print(f"Current DLL: {dll}")
    print("-" * 55)

    # 4. Deleting from ends
    print(f"delete_first() -> {dll.delete_first()}")
    print(f"delete_last()  -> {dll.delete_last()}")
    print(f"Final DLL: {dll}")
