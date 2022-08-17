#!/usr/bin/env python3

from random import shuffle

from solution import SolutionBase

def patch(string, substring, index, length):
    """Replace a portion of a string."""
    return string[:index] + substring + string[index + length:]

def indices(string, substring):
    """Yield the indices of all occurences of the substring within the string."""

    for i in range(len(string)):
        if string[i:].startswith(substring):
            yield i

class Solution(SolutionBase):
    def part_one(self):
        replacements_string, molecule = self.input.split("\n\n")
        replacements = [tuple(s.strip() for s in string.split("=>")) for string in replacements_string.split("\n")]
        molecules = set()
        for source, replacement in replacements:
            for index in indices(molecule, source):
                replaced = patch(molecule, replacement, index, len(source))
                molecules.add(replaced)
        return len(molecules)

    def part_two(self):
        replacements_string, target = self.input.split("\n\n")
        replacements = [tuple(s.strip() for s in string.split("=>")) for string in replacements_string.split("\n")]
        return len(list(filter(lambda c: c.isupper(), target))) - target.count("Rn") - target.count("Ar") - 2 * target.count("Y") - 1

solution = Solution.instantiate(19)

if __name__ == "__main__":
    solution.run()
