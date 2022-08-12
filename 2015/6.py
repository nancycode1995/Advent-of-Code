#!/usr/bin/env python3

from abc import ABC, abstractmethod
from itertools import product
from numpy import prod

from advent import solution

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
    return product(*[list(range(ax, bx + 1)) for ax, bx in zip(a, b)]), string

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

    def execute(self, lights):
        for index in self.lights_range:
            lights[index] = self.function(lights[index])

class InstructionToggle(Instruction):
    """Instruction which toggles the state of the lights."""

    def function(self, state):
        return not state

class InstructionEnable(Instruction):
    """Instruction which turns on the lights."""

    def function(self, state):
        return True

class InstructionDisable(Instruction):
    """Instruction which turns off the lights."""

    def function(self, state):
        return False

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
            print(f"Executing instruction {i + 1}/{len(self.instructions)} ({i / len(self.instructions)}%)")
            instruction.execute(lights)

@solution("6.txt", "Part 1")
def solve(string):
    lights = Grid.with_dimensions(False, 1000, 1000)
    Program.from_string(string).execute(lights)
    return lights.values.count(False)

