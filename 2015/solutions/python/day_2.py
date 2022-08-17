#!/usr/bin/env python3

from itertools import combinations
from numpy import prod

from solution import SolutionBase

class Present:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    @classmethod
    def from_string(cls, string):
        """Parse a string designating the dimensions of a present box."""
        return cls(*map(int, string.split("x")))

    @property
    def dimensions(self):
        return self.length, self.width, self.height

    @property
    def sides(self):
        return list(combinations(self.dimensions, 2))

    @property
    def required_paper(self):
        surface_areas = list(map(prod, self.sides))
        smallest = sorted(surface_areas)[0]
        return 2 * sum(surface_areas) + smallest

    @property
    def volume(self):
        return prod(self.dimensions)

    @property
    def required_ribbon(self):
        perimeters = list(map(sum, self.sides))
        smallest = sorted(perimeters)[0]
        return 2 * smallest + self.volume

    def __str__(self):
        return "x".join(list(map(str, self.dimensions)))

class Solution(SolutionBase):
    def part_one(self):
        presents = map(Present.from_string, self.input.split())
        return sum([present.required_paper for present in presents])

    def part_two(self):
        presents = map(Present.from_string, self.input.split())
        return sum([present.required_ribbon for present in presents])

solution = Solution.instantiate(2)

if __name__ == "__main__":
    solution.run()
