"""Test for the functions in utils."""

__author__ = "730572598"


from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """List is empty."""
    list: list[int] = []
    assert only_evens(list) == []


def test_only_evens_all_odds() -> None:
    """All odds."""
    list: list[int] = [1, 3, 5]
    assert only_evens(list) == []


def test_only_evens_mixed_evens_odds() -> None:
    """Mixed evens and odds."""
    list: list[int] = [1, 2, 3, 4]
    assert only_evens(list) == [2, 4]


def test_only_evens_all_evens() -> None:
    """All evens."""
    list: list[int] = [4, 4, 4]
    assert only_evens(list) == [4, 4, 4]


def test_concat_combining() -> None:
    """Normal combination of two lists."""
    list_one: list[int] = [1, 2, 3]
    list_two: list[int] = [4, 5, 6]
    assert concat(list_one, list_two) == [1, 2, 3, 4, 5, 6]


def test_concat_list_one_empty() -> None:
    """Combining an empty first list with the second list."""
    list_one: list[int] = []
    list_two: list[int] = [1, 2, 3]
    assert concat(list_one, list_two) == [1, 2, 3]


def test_concat_list_two_empty() -> None:
    """Combining the first list with an empty second list."""
    list_one: list[int] = [1, 2, 3]
    list_two: list[int] = []
    assert concat(list_one, list_two) == [1, 2, 3]


def test_concat_both_lists_empty() -> None:
    """Combining two empty lists."""
    list_one: list[int] = []
    list_two: list[int] = []
    assert concat(list_one, list_two) == []


def test_sub_empty_list_same_start_end() -> None:
    """An empty list and the same start and end ints."""
    a_list: list[int] = []
    start: int = 0
    end: int = 0
    assert sub(a_list, start, end) == []


def test_sub_same_start_and_end() -> None:
    """Same start and end ints."""
    a_list: list[int] = [1, 2, 3]
    start: int = 0
    end: int = 0
    assert sub(a_list, start, end) == []


def test_sub_empty_list() -> None:
    """Iterating through an emtpy list."""
    a_list: list[int] = []
    start: int = 1
    end: int = 3
    assert sub(a_list, start, end) == []


def test_sub_negative_start() -> None:
    """Iterating through a list with a negative starting point."""
    a_list: list[int] = [10, 20, 30, 40]
    start: int = -1
    end: int = 3
    assert sub(a_list, start, end) == [10, 20, 30]


def test_sub_greater_than_length_end() -> None:
    """End point greater than the length of the list."""
    a_list: list[int] = [10, 20, 30, 40]
    start: int = 0
    end: int = 5
    assert sub(a_list, start, end) == [10, 20, 30, 40]


def test_sub_normal() -> None:
    """Normal run of sub."""
    a_list: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 3
    assert sub(a_list, start, end) == [20, 30]
