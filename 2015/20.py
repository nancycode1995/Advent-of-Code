#!/usr/bin/env python3

from itertools import count

from advent import solution

@solution("20.txt", "Part 1")
def solve(string):
    min_presents = int(string) / 10
    for i in count(1):
        if sum(filter(lambda x: i % x == 0, range(1, i + 1))) >= min_presents:
            return i
