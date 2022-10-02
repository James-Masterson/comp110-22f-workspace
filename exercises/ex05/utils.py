"""This is where the functions for ex05 will be written."""

__author__ = "730572598"


def only_evens(list: list[int]) -> int:
    """This function will integrate through a list and output all of the even numbers."""
    i: int = 0
    evens_list: list[int] = []
    while (i < len(list)):
        if (list[i] % 2 == 0):
            evens_list.append(list[i])
        i += 1
    return evens_list


def concat(list_one: list[int], list_two: list[int]) -> int:
    """This functions combines two lists into one without modifying either of the original lists."""
    i: int = 0
    combined_list: list[int] = []
   
    while (i < len(list_one)):
        combined_list.append(list_one[i])
        i += 1
    
    i = 0
    
    while (i < len(list_two)):
        combined_list.append(list_two[i])
        i += 1
    return combined_list


def sub(a_list: list[int], start: int, end: int) -> int:
    """This function prints out all numbers of a list between an established starting int and an  established ending int, non-inclusive."""
    sub_list: list[int] = []
    
    if (len(a_list) == 0):
        return sub_list
    else:
        if (start < 0):
            start = 0
        if (end > len(a_list)):
            end = len(a_list)
        
        while (start < end):
            sub_list.append(a_list[start])
            start += 1
    return sub_list
