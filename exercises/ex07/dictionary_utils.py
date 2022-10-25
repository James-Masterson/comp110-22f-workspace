"""This is where we will test the functions defined within the dictionary file."""

__author__ = "730572598"


from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_empty_dict() -> None:
    """Dict empty."""
    data: dict[str, str] = {}
    assert invert(data) == {}


def test_invert_repeat_keys() -> None:
    """Repeat keys.""" 
    data: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
    assert invert(data) == KeyError("No worky.")


def test_invert_normal_dict() -> None:
    """Normal test."""
    data: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(data) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_one_value() -> None:
    """Inverting a dictionary of one value."""
    data: dict[str, str] = {'a': 'z'}
    assert invert(data) == {'z': 'a'}


def test_favorite_color_empty_dict() -> None:
    """Dict empty."""
    colors: dict[str, str] = {}
    assert favorite_color(colors) == ""


def test_favorite_color_one_each() -> None:
    """One of each color."""
    colors: dict[str, str] = ({"Marc": "yellow", "Ezri": "blue"})
    assert favorite_color(colors) == 'yellow'


def test_favorite_color_normal_test() -> None:
    """Normal test of favorite color function."""
    colors: dict[str, str] = ({"Marc": "blue", "Ezri": "yellow", "James": "blue", "Ezri": "yellow"})
    assert favorite_color(colors) == 'blue'


def test_favorite_color_one_value() -> None:
    """Testing with one value in dictionary."""
    colors: dict[str, str] = ({"Marc": "yellow"})
    assert favorite_color(colors) == 'yellow'


def test_count_empty() -> None:
    """Empty input list."""
    input_list: list[str] = []
    assert count(input_list) == {}


def test_count_one_of_each() -> None:
    """One of each values."""
    input_list: list[str] = ["hi", "we", "yo", "be"]
    assert count(input_list) == {'hi': 1, 'we': 1, 'yo': 1, 'be': 1}


def test_count_multiples() -> None:
    """Multiple of certain values."""
    input_list: list[str] = ["hi", "we", "yo", "be", "hi", "we"]
    assert count(input_list) == {'hi': 2, 'we': 2, 'yo': 1, 'be': 1}


def test_count_one_value() -> None:
    """One value in list."""
    input_list: list[str] = ["hi"]
    assert count(input_list) == {'hi': 1}
