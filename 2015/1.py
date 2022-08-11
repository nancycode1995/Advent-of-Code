#!/usr/bin/env python3

from numpy import cumsum

from advent import solution

def translate(string):
    """Return a map from the input string characters to corresponding integer 1 or -1."""
    
    mapping = {"(": 1, ")": -1}
    return map(mapping.__getitem__, string)

@solution("1.txt", "Part 1")
def part_1(string):
    return sum(translate(string))

@solution("1.txt", "Part 2")
def part_1(string):
    for i, n in enumerate(cumsum(list(translate(string)))):
        if n < 0:
            return i + 1
