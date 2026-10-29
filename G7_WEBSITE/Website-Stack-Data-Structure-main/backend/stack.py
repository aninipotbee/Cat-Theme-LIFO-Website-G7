"""BACKEND / STUDENT MODIFICATION ZONE: backend/stack.py.

LIFO Stack backed by a Python list.
The END of the list is the TOP of the stack, so push/pop are O(1).
to_list() returns values from oldest/bottom to newest/top, as the
database contract requires.
"""

class Stack:
    """Last-In, First-Out stack of removed item IDs."""

    def __init__(self, items=None):
        self._items = list(items) if items is not None else []

    def push(self, item):
        """Record one removed item's ID on top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the NEWEST ID (top of the stack)."""
        if self.is_empty():
            raise IndexError("The recovery tray is empty.")
        return self._items.pop()

    def peek(self):
        """Return the top ID without removing it."""
        if self.is_empty():
            raise IndexError("The recovery tray is empty.")
        return self._items[-1]

    def is_empty(self):
        """True when there are no recovery records."""
        return len(self._items) == 0

    def size(self):
        """Number of recovery records."""
        return len(self._items)

    def to_list(self):
        """Return a NEW list, bottom -> top, ready to save in SQLite."""
        return list(self._items)


HistoryBuffer = Stack