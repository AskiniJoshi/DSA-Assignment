"""
Assignment 3 - Part D: Linked Lists
Question D6: Favorites List ADT Implementation

Favorites List ADT Specification:
    Maintains a collection of elements while keeping track of the access frequency
    of each element.

Stored Item Fields:
    Each stored record contains an inner _Item composite object:
        - _value: The actual element payload (e.g., URL, song, file name).
        - _count: An integer tracking how many times access(e) was called on this item.

Supported Operations & Update Behaviour:
--------------------------------------------------------------------------------------
Operation     Behaviour
--------------------------------------------------------------------------------------
access(e)     - Searches for item with value e.
              - If found: increments item._count by 1.
              - If not found: creates new _Item(e, count=1) and appends it to list.
              - In count-sorted list: walks the item forward past any predecessor
                with a smaller count to keep the list in non-increasing count order.

remove(e)     - Searches for item with value e and removes it from the list.
              - Raises ValueError if e is not present.

top(k)        - Returns an iterable containing the top k most accessed elements.
              - Raises ValueError if k <= 0 or k > len(list).
"""

class FavoritesList:
    """List of elements ordered by access count (non-increasing)."""

    class _Item:
        """Composite item holding element and its access frequency."""
        __slots__ = '_value', '_count'

        def __init__(self, value):
            self._value = value
            self._count = 0

        def __repr__(self):
            return f"({self._value}: {self._count})"

    def __init__(self):
        """Create an empty favorites list."""
        self._data = []  # Underlying sequence of _Item references

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def _find_item(self, e):
        """Helper to find index of item with value e, or -1 if absent."""
        for i, item in enumerate(self._data):
            if item._value == e:
                return i
        return -1

    def access(self, e):
        """
        Access element e. Increments its count (or adds it if new),
        and maintains non-increasing sorted count order.
        """
        idx = self._find_item(e)
        if idx == -1:
            # New item: initialize with count 1
            item = self._Item(e)
            item._count = 1
            self._data.append(item)
            idx = len(self._data) - 1
        else:
            item = self._data[idx]
            item._count += 1

        # Move item forward towards the head while predecessor count is smaller
        while idx > 0 and self._data[idx - 1]._count < item._count:
            self._data[idx] = self._data[idx - 1]
            idx -= 1
        self._data[idx] = item

    def remove(self, e):
        """Remove element e from the favorites list."""
        idx = self._find_item(e)
        if idx == -1:
            raise ValueError(f"Element '{e}' not found in favorites list.")
        return self._data.pop(idx)._value

    def top(self, k):
        """
        Generate sequence of top k most accessed elements.
        """
        if not 1 <= k <= len(self._data):
            raise ValueError(f"k={k} is out of valid range [1, {len(self._data)}].")
        return [self._data[i]._value for i in range(k)]

    def get_entries(self):
        """Return list of (element, count) tuples."""
        return [(item._value, item._count) for item in self._data]

    def __repr__(self):
        return f"FavoritesList({self._data})"


if __name__ == "__main__":
    print("=" * 70)
    print("TESTING FAVORITES LIST ADT (Part D - Question 6)")
    print("=" * 70)

    fav = FavoritesList()
    print(f"Initial empty list: {fav}")
    print("-" * 55)

    # 1. Simulating web page or song accesses
    print("Simulating sequence of accesses:")
    access_sequence = [
        "google.com", "python.org", "google.com", "github.com",
        "python.org", "google.com", "stackoverflow.com", "github.com",
        "google.com", "wikipedia.org", "python.org", "google.com"
    ]

    for url in access_sequence:
        fav.access(url)
        print(f"  Accessed '{url:<18}' -> Status: {fav.get_entries()}")

    print("-" * 55)
    print(f"Full Favorites List: {fav}")
    print("-" * 55)

    # 2. Querying top(k)
    print("Querying Top Elements:")
    print(f"  Top 1: {fav.top(1)}")
    print(f"  Top 3: {fav.top(3)}")
    print(f"  Top 5: {fav.top(5)}")
    print("-" * 55)

    # 3. Removing an element
    print("Removing 'github.com':")
    fav.remove("github.com")
    print(f"  After removal: {fav.get_entries()}")
    print(f"  New Top 3:     {fav.top(3)}")
    print("-" * 55)

    # 4. Error handling
    print("Testing error handling:")
    try:
        fav.remove("nonexistent.org")
    except ValueError as e:
        print(f"  Caught expected error on remove: '{e}'")

    try:
        fav.top(100)
    except ValueError as e:
        print(f"  Caught expected error on top(100): '{e}'")
