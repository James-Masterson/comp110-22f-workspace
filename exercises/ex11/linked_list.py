"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730572598"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next == None:
            return head.data
        else:
            return last(head.next)

def value_at(head: Optional[Node], index: int, index_two: int = 0) -> int:
    """Given a head Optional[Node] and an index int as inputs, return the data of the Node stored at the given index, or raise an IndexError if the index does not exist."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    else:
        if index == index_two:
            return head.data
        else:
            index_two += 1
            return value_at(head.next, index, index_two)

def max(head: Node) -> int:
    """Weird."""
    if head.next is None:
        return head.data
    else:
        print(max(head.node))
    # else:
    #     raise ValueError("Can't call max with None.")