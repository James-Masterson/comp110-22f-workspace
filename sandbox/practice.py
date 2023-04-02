def odd_and_even(end: list[int]) -> list[int]:
    """Practice."""
    i: int = 0
    final: list[int] = []
    while i < len(end):
        
        if end[i] % 2 != 0 and i % 2 == 0:
            final.append(end[i])

        i += 1

    return final

print(odd_and_even([1, 2, 1, 3, 4]))


def value_exists(test_dict: dict[str, int], test_val: int) -> bool:
    """Practice."""

    flag: bool = False
    for key in test_dict:
        if test_dict[key] == test_val:
            flag = True
    return flag


print(value_exists({"a" : 2, "b": 5, "c" : 8}, 5))


def short_words(test: list[str]) -> list[str]:
    """Practice."""

    i: int = 0
    my_list: list[str] = []
    
    while i < len(test):
        if len(test[i]) < 5:
            my_list.append(test[i])
        else: 
            print(test[i] + " is too long!")
        
        i += 1

    return my_list


print(short_words(["cat", "dog", "doggo"]))