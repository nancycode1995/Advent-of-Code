#!/usr/bin/env python3

from itertools import count
from hashlib import md5

from solution import SolutionBase

def find_hash(secret, match_function):
    inputs = (f"{secret}{x}".encode("ascii") for x in count())
    hashed = (md5(hash_input).hexdigest() for hash_input in inputs)
    pairs = zip(count(), hashed)
    valid = filter(lambda x: match_function(x[1]), pairs)
    return next(valid)[0]

class Solution(SolutionBase):
    def part_one(self):
        matches = lambda hashed: str(hashed).startswith("00000")
        return find_hash(self.input, matches)

    def part_two(self):
        matches = lambda hashed: str(hashed).startswith("000000")
        return find_hash(self.input, matches)

solution = Solution.instantiate(4)

if __name__ == "__main__":
    solution.run()
