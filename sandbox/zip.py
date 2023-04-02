def zip(keys: list[str], values: list[str]) -> dict[str, int]:
    """Weird."""
    i: int = 0
    final: dict[str, int] = {}
    
    while i < len(keys):
        final[keys[i]] = values[i]
        i += 1

    return final


print(zip([1, 2, 3], [4, 5, 6]))