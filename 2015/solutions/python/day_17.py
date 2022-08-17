#!/usr/bin/env python3

from itertools import combinations

from solution import SolutionBase

class Solution(SolutionBase):
    def part_one(self):
        capacities = list(map(int, self.input.split("\n")))
        combos = sum([list(combinations(capacities, r + 1)) for r in range(len(capacities))], [])
        return len(list(filter(lambda x: sum(x) == 150, combos)))

    def part_two(self):
        capacities = list(map(int, self.input.split("\n")))
        combos = sum([list(combinations(capacities, r + 1)) for r in range(len(capacities))], [])
        fitting_combos = list(filter(lambda x: sum(x) == 150, combos))
        fewest_needed = sorted(map(len, fitting_combos))[0]
        return len(list(filter(lambda x: len(x) == fewest_needed, fitting_combos)))

solution = Solution.instantiate(17)

if __name__ == "__main__":
    solution.run()
