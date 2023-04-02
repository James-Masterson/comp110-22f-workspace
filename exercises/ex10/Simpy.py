"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730572598"


class Simpy:
    """Manual functions that recreate/copy the Numpy library."""
    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Its purpose is to initialize the values attribute of the newly constructed Simpy object to the argument passed in."""
        self.values = values

    def __repr__(self) -> str:
        """Define a method in `Simpy` named `__repr__` that takes no arguments and returns a `str`."""
        return f"Simpy({self.values})"

    def fill(self, float_number: float, amount: int) -> None:
        """Its purpose is to _fill_ a Simpy's values with a specific number of repeating values."""
        self.values = []
        for _ in range(amount):
            self.values.append(float_number)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Its purpose is to fill in the values attribute with range of values, like the range built-in function, but in terms of floats."""
        assert step != 0.0
        while start < stop:
            self.values.append(start)
            start += step
        else: 
            while stop < start:
                self.values.append(start)
                start += step
            
    def sum(self) -> float:
        """Its purpose is to compute and return the sum of all items in the values attribute."""
        result: float = 0.0
        i: int = 0
        for i in range(len(self.values)):
            result += self.values[i]
            i += 1
        return result

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """You will implement `__add__` such that the right-hand side operand of an addition expression can be _either_ a Simpy object _or_ a float value using a Union type. The __add__ method should return a new Simpy object and _should not_ mutate the object the method is called on."""
        result: Simpy = Simpy([])

        if isinstance(rhs, float):
            for num in self.values:
                result.values.append(num + rhs)
        else: 
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Next, you will add the ability to use the _power operator_ (**) in conjunction with Simpy objects and floats."""
        result: Simpy = Simpy([])

        if isinstance(rhs, float):
            for num in self.values:
                result.values.append(num ** rhs)
        else: 
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Next, you will add the ability to produce a _mask_, or a list[bool], based on the equality of each item in the values attribute with some other Simpy object or a float value."""
        result: list[bool] = []

        if isinstance(rhs, float):
            for num in range(len(self.values)):
                if self.values[num] == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else: 
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Next, you will add the ability to produce a _mask_, or a list[bool], based on the equality of each item in the values attribute with some other Simpy object or a float value."""
        result: list[bool] = []

        if isinstance(rhs, float):
            for num in range(len(self.values)):
                if self.values[num] > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else: 
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Next, you will add the ability to use the _subscription_ operator with Simpy objects. To add _subscription notation_ support to objects of classes you design, you must implement the special method named __getitem__."""
        list_one: list[bool] = []
        result_simpy: Simpy = Simpy([])
        
        if isinstance(rhs, int):
            for num in range(len(self.values)):
                if self.values[num] == rhs:
                    list_one.append(True)
                else:
                    list_one.append(False)
            for i in range(len(list_one)):
                if list_one[i] is True:
                    result_simpy.values.append(self.values[i])
            result: float = 0.0
            result = self.values[rhs]
            return result
        else:
            for x in range(len(self.values)):
                if rhs[x] is True:
                    result_simpy.values.append(self.values[x])  

        return result_simpy

    