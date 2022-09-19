"""EX03 - Structured Wordle - The final step into creating Wordle."""

__author__ = "730572598"


def all(list: list[int], test: int) -> bool:
    """This function determines if a number is contained within a list and outputs True or False."""
    i: int = 0
    if (len(list) == 0):
        return False
    else:
        while (i < len(list)):
            if (list[i] != test):
                return False
            i += 1
        return True


def max(nums: list[int]) -> int:
    """This function outputs the max number in a list."""
    if (len(nums) == 0):
        raise ValueError("max() arg is an empty List")
    else:
        i: int = 0
        highest_int: int = nums[0]
        while (i < len(nums)):
            if (nums[i] > highest_int):
                highest_int = nums[i]
            i += 1
    return highest_int


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """This function checks if two lists are deeply equal to each other."""
    i: int = 0
    all_chars_equal: bool = False
    if (len(first_list) + len(second_list) == 0):
        return True
    else:
        if (len(first_list) == 0):
            return False
        if (len(second_list) == 0):
            return False
        if (len(first_list) == len(second_list)):
            while (i < len(first_list)):
                if (first_list[i] == second_list[i]):
                    all_chars_equal = True
                else:
                    all_chars_equal = False
                i += 1
            if (all_chars_equal is True):
                return True
            else:
                return False
        else:
            return False