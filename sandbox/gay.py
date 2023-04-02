def reverse_multiply(list_one: list[int]) -> list:
    result: list[int] = []
    i: int = len(list_one) - 1
    while i >= 0:
        list_one[i] *= 2
        result.append(list_one[i])
        i -= 1
    return result 

def free_biscuits(dict_one: dict[str, list[int]]) -> dict[str, bool]:
    result: dict[str, bool] = {}
    for key in dict_one:
        i: int = 0
        total: int = 0
        while i < len(dict_one[key]):
            total += dict_one[key][i]
            i += 1
        if total < 100:
            result[key] = False
        else: 
            result[key] = True
    return result

def multiples(list_one: list[int]) -> list[bool]:
    i: int = 0
    j: int = i - 1
    result: list[bool] = []
    while i < len(list_one):
        if i == 0:
            j = len(list_one) - 1
            if list_one[i] % list_one[j] == 0:
                result.append(True)
            else:
                result.append(False)
            i += 1
        else:
            j = i - 1
            if list_one[i] % list_one[j] == 0:
                result.append(True)
            else:
                result.append(False)
            i += 1
    return result

def merge_lists(list_one: list[str], list_two: list[int]) -> dict[str, int]:
    result: dict[str, int] = {}
    i: int = 0
    if len(list_one) != len(list_two):
        return result
    else:
        while i < len(list_one):
            result[list_one[i]] = list_two[i]
            i += 1
    return result
