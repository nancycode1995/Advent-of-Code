#!/usr/bin/env python3

from solutions.solution import SolutionBase

def encode(string):
    def encode_character(character):
        if character == "\\":
            return "\\\\"
        if character == "\"":
            return "\\\""
        else:
            return character
    return '"' + "".join(list(map(encode_character, string))) + '"'

class Solution(SolutionBase):
    def part_one(self):
        # a totally cheaty and non production safe solution!
        literals = self.input.split()
        strings = list(map(eval, literals))
        lengths_literals = list(map(len, literals))
        lengths_strings = list(map(len, strings))
        total_literals = sum(lengths_literals)
        total_strings = sum(lengths_strings)
        return total_literals - total_strings

    def part_two(self):
        literals = self.input.split()
        representations = list(map(encode, literals))
        lengths_literals = list(map(len, literals))
        lengths_representations = list(map(len, representations))
        total_literals = sum(lengths_literals)
        total_representations = sum(lengths_representations)
        return total_representations - total_literals

solution = Solution.instantiate(8)

if __name__ == "__main__":
    solution.run()
