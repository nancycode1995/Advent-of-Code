#!/usr/bin/env python3

from numpy import cumsum

from solution import SolutionBase

def translate(string):
    """Return a map from the input string characters to corresponding integer 1 or -1."""
    
    mapping = {"(": 1, ")": -1}
    return map(mapping.__getitem__, string)

class Solution(SolutionBase):
    def part_one(self):
        #return sum(translate(self.input))
        return self.input.count("(") - self.input.count(")");

    def part_two(self):
        for i, n in enumerate(cumsum(list(translate(self.input)))):
            if n < 0:
                return i + 1

solution = Solution.instantiate(1)

if __name__ == "__main__":
    solution.run()
