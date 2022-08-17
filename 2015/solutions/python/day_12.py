#!/usr/bin/env python3

import json

from solution import SolutionBase

def count(data, ignore=None):
    if type(data) == list:
        return sum(count(item, ignore) for item in data)
    elif type(data) == dict:
        if ignore and ignore in list(data.values()):
            return 0
        else:
            return count(list(data.values()), ignore)
    elif type(data) == int:
        return data
    else:
        return 0

class Solution(SolutionBase):
    def part_one(self):
        data = json.loads(self.input)
        return count(data)

    def part_two(self):
        data = json.loads(self.input)
        return count(data, "red")

solution = Solution.instantiate(12)

if __name__ == "__main__":
    solution.run()
