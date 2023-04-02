"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730572598"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Returns the distance between the Point object the method was called on and some other Point object passed in as a parameter."""
        result: float = sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))
        return result


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction
    
    def tick(self) -> None:
        """Updates the cell's position each tick."""
        self.location = self.location.add(self.direction)
        if self.is_infected() is True:
            self.sickness += 1
        if self.sickness >= constants.RECOVERY_PERIOD:
            self.immunize()
    
    def contract_disease(self) -> None:
        """Assings the INFECTED constant to the sickness variable."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """It should return True when the cell's sickness attribute is equal to Vulnerable and False otherwise."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """It should return True when the cell's sickness attribute is equal to INFECTED and False otherwise."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def color(self) -> str:
        """Define a method of a Cell named color. It should return "gray" if the Cell is vulnerable, and any other color string of your choosing if the Cell is infected."""
        if self.is_vulnerable() is True:
            return "gray"
        if self.is_infected() is True:
            return "lime"
        if self.is_immune() is True:
            return "red"

    def contact_with(self, cell: Point):
        """Define a method on the Cell class that can be given another Cell object as a parameter. If either of the Cell objects is infected and the other is vulnerable, then the other should become infected."""
        if self.is_infected() and cell.is_vulnerable() is True:
            self.contract_disease()
            cell.contract_disease()
        else:
            if self.is_vulnerable() and cell.is_infected() is True:
                self.contract_disease()
                cell.contract_disease()
            else: 
                if self.is_immune() and cell.is_infected() is True:
                    self.immunize()
                else:
                    if self.is_infected and cell.is_immune() is True:
                        cell.immunize()
                    else:
                        if self.is_immune() and cell.is_vulnerable() is True:
                            self.immunize()
                        else:
                            if self.is_vulnerable() and cell.is_immune() is True:
                                cell.immunize() 
    
    def immunize(self):
        """Add a method to Cell named immunize that assigns the constant IMMUNE to the sickness attribute of the Cell."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Add a method to Cell named is_immune that returns True when the Cell object's sickness attribute is equal to the IMMUNE constant."""
        if self.sickness == constants.IMMUNE:
            return True


class Model:
    """The state of the simulation."""
    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        i: int = 0
        j: int = 0
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if infected >= cells or infected <= 0:
                raise ValueError("Some number of the Cell objects must begin infected.")
            elif immune >= cells or immune < 0:
                raise ValueError("Some number of the Cell objects must begin infected.")
            elif immune + infected > cells:
                raise ValueError("Some number of the Cell objects must begin infected.")
            elif i < infected:
                cell.contract_disease()
                i += 1
            elif j < immune:
                cell.immunize()
                j += 1
            
            self.population.append(cell)

    def check_contacts(self) -> None:
        """Its purpose is to compare the distance between every two Cell objects' location attributes in the population."""
        for i in range(len(self.population)):
            for j in range(i + 1, len(self.population)):
                cell_one: Cell = self.population[i]
                cell_two: Cell = self.population[j]
                if cell_one.location.distance(cell_two.location) < constants.CELL_RADIUS:
                    cell_one.contact_with(cell_two)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        i: int = 0
        j: int = 0
        for j in range(len(self.population)):
            if Cell.is_immune(self.population[j]) is True:
                i += 1
            if Cell.is_vulnerable(self.population[j]) is True:
                i += 1
        while i < len(self.population):
            return False
        else:
            return True