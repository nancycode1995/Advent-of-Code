#!/usr/bin/env python3

from itertools import groupby

from solutions.solution import SolutionBase

def look_and_say(string, iterations=1):
    for i in range(iterations):
        #print(f"Iteration {i}/{iterations} = {len(string)}")
        string = "".join([f"{len(list(group))}{key}" for key, group in groupby(string)])
    return string

class Solution(SolutionBase):
    def part_one(self):
        return len(look_and_say(self.input, 40))

    def part_two(self):
        return len(look_and_say(self.input, 50))

solution = Solution.instantiate(10)

if __name__ == "__main__":
    solution.run()
