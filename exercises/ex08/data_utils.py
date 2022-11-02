"""Dictionary related utility functions."""

__author__ = "730572598"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(data_table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. dict[str, list[str]]) table with only the first N (a parameter) rows of data for each column."""
    if num_rows > len(data_table):
        return data_table
    result: dict[str, list[str]] = {}
    for key in data_table: 
        result_list: list[str] = []
        i: int = 0
        while i < num_rows:
            result_list.append(data_table[key][i])
            i += 1
        result[key] = result_list
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. dict[str, list[str]]) table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for i in names:
        result[i] = table[i]
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. dict[str, list[str]]) table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for key in table_one:
        result[key] = table_one[key]
    for key in table_two:
        if key in result:
            result[key] += table_two[key]
        else:
            result[key] = table_two[key]

    return result


def count(data_table: list[str]) -> dict[str, int]:
    """Given a list[str], this function will produce a dict[str, int] where each key is a unique value in the given list and each value associated is the _count_ of the number of times that value appeared in the input list."""
    if len(data_table) == 0:
        raise ("Empty list passed through")
    elif len(data_table) == 1:
        return {data_table[0]: 1}
    else:
        result: dict[str, int] = {}
        for key in data_table:
            if key in result:
                result[key] += 1
            else:
                result[key] = 1

        return result
