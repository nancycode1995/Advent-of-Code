#!/usr/bin/env python3

# TODO: rewrite this one! This implementation is too slow, and too complicated. The problem can be solved much more simply and effeciently.

from abc import ABC, abstractmethod
from itertools import product
from numpy import prod

from solution import SolutionBase

def consume(string, expected):
    """Consume the first of any expected token strings from a string and return the token and the remaining string."""

    string = string.strip()
    for token in expected:
        if string.startswith(token):
            return token, string[len(token):]

    return None, string

def consume_coordinates(string):
    tokens = string.split(maxsplit=1)
    token = tokens[0]
    rest = tokens[1] if len(tokens) > 1 else ""
    return list(map(int, token.split(","))), rest

def consume_lights_range(string):
    """Parse from a string the part of the instruction that designates the range of lights."""

    a, string = consume_coordinates(string)
    _, string = consume(string, ["through"])
    b, string = consume_coordinates(string)
    return [range(ax, bx + 1) for ax, bx in zip(a, b)], string

class Grid:
    """An n-dimensional array."""

    def __init__(self, dimensions, values=None):
        self.dimensions = dimensions
        self.values = values or []

    @classmethod
    def with_dimensions(cls, value, *dimensions):
        return cls(dimensions, [value] * prod(dimensions))

    def get_index(self, coordinates):
        return int(sum(coordinate * prod(self.dimensions[:i]) for i, coordinate in enumerate(coordinates)))

    def __getitem__(self, coordinates):
        return self.values[self.get_index(coordinates)]

    def __setitem__(self, coordinates, value):
        self.values[self.get_index(coordinates)] = value

    def apply_to_range(self, function, lights_range):
        bases = [prod(self.dimensions[:i]) for i in range(len(self.dimensions))]
        for coordinates in product(*lights_range):
            index = int(sum(coordinate * base for coordinate, base in zip(coordinates, bases)))
            self.values[index] = function(self.values[index])

    def __str__(self):
        # TODO do this nicely! (I just did it as an ad hoc debugging tool
        output = ""
        for y in range(self.dimensions[1]):
            i = y * self.dimensions[0]
            output += str(self.values[i:i + self.dimensions[0]]) + "\n"
        return output

class Instruction(ABC):
    """A light state manipulation program instruction."""

    def __init__(self, lights_range):
        self.lights_range = lights_range

    @classmethod
    def from_string(self, string):
        """Compile an instruction."""

        opcodes = {
                "toggle": InstructionToggle,
                "turn on": InstructionEnable,
                "turn off": InstructionDisable,
                }

        opcode, string = consume(string, opcodes.keys())
        lights_range, string = consume_lights_range(string)
        return opcodes[opcode](lights_range)

    @abstractmethod
    def function(self, state):
        """Given the state of a light, return the new state."""
        ...

    @property
    @abstractmethod
    def opcode(self) -> str:
        ...

    def execute(self, lights):
        lights.apply_to_range(self.function, self.lights_range)

    def __str__(self):
        a_string = ",".join(str(dimension_range.start) for dimension_range in self.lights_range)
        b_string = ",".join(str(dimension_range.stop) for dimension_range in self.lights_range)
        range_string = f"{a_string} through {b_string}"
        return f"{self.opcode} {range_string}"

class InstructionToggle(Instruction):
    """Instruction which toggles the state of the lights. (Actually it increases the brightness by 2.)"""

    def function(self, state):
        if type(state) == bool:
            return not state
        else: return state + 2

    @property
    def opcode(self):
        return "toggle"

class InstructionEnable(Instruction):
    """Instruction which turns on the lights. (Actually it increases brightness by 1.)"""

    def function(self, state):
        if type(state) == bool:
            return True
        else: return state + 1

    @property
    def opcode(self):
        return "turn on"

class InstructionDisable(Instruction):
    """Instruction which turns off the lights. (Actually it decreases brightness by 1.)"""

    def function(self, state):
        if type(state) == bool:
            return False
        else: return max(0, state - 1)

    @property
    def opcode(self):
        return "turn off"

class Program:
    """A program that instructs how to manipulate the state of the lights."""

    def __init__(self, instructions):
        self.instructions = instructions

    @classmethod
    def from_string(cls, string):
        """Compile a program string."""

        return cls([Instruction.from_string(line) for line in string.split('\n')])

    def execute(self, lights):
        """Run the program given the lights to manipulate."""

        for i, instruction in enumerate(self.instructions):
            #print(f"Executing instruction {i + 1}/{len(self.instructions)} ({i / len(self.instructions):.2}%)")
            #print(instruction)
            instruction.execute(lights)
            #print(lights)

class Solution(SolutionBase):
    def part_one(self):
        lights = Grid.with_dimensions(False, 1000, 1000)
        Program.from_string(self.input).execute(lights)
        return lights.values.count(True)

    def part_two(self):
        lights = Grid.with_dimensions(0, 1000, 1000)
        Program.from_string(self.input).execute(lights)
        return sum(lights.values)

solution = Solution.instantiate(6)

if __name__ == "__main__":
    solution.run()
