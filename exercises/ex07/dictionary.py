"""This is where the functions invert, favorite_color, and count will be defined."""

__author__ = "730572598"


def invert(data: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values to that the value becomes the key and vice versua."""
    result: dict[str, str] = {}
    for key in data:
        if data[key] in result:
            raise KeyError("No worky!")
        result[data[key]] = key

    return result


def favorite_color(colors: dict[str, str]) -> str:
    """This function returns the most common color in a dictionary."""
    color_list: list[str] = []
    i: int = 0
    x: int = 0
    current_counter: int = 0
    stored_count: int = 0
    color_value: str = ""
    popular_color: str = ""

    for key in colors:
        color_list.append(colors[key])

    while (x < len(color_list)):
        color_value = color_list[x]
        while (i < len(color_list)):
            if (color_list[i] == color_value):
                current_counter += 1
            if (current_counter > stored_count):
                stored_count = current_counter
                popular_color = color_list[x]
            i += 1
        current_counter = 0
        i = 0    
        x += 1
    
    return popular_color


def count(input_list: list[str]) -> dict[str, int]:
    """This function creates a new dictionary and takes the strings from the lists and sets them as the keys in the dict and assigns them values according to how many times they appear."""
    updated_dict: dict[str, int] = {}
    i: int = 0
    x: int = 0
    counter: int = 0
    value: str = ""

    while (x < len(input_list)):
        value = input_list[x]
        while (i < len(input_list)):
            if (input_list[i] == value):
                counter += 1
            i += 1
        updated_dict[input_list[x]] = counter
        counter = 0
        i = 0    
        x += 1
        
    return updated_dict
