#!/usr/bin/env python3

from itertools import combinations

from advent import solution

@solution("17.txt", "Part 1")
def solve(string):
    capacities = list(map(int, string.split("\n")))
    combos = sum([list(combinations(capacities, r + 1)) for r in range(len(capacities))], [])
    return len(list(filter(lambda x: sum(x) == 150, combos)))

@solution("17.txt", "Part 2")
def solve(string):
    capacities = list(map(int, string.split("\n")))
    combos = sum([list(combinations(capacities, r + 1)) for r in range(len(capacities))], [])
    fitting_combos = list(filter(lambda x: sum(x) == 150, combos))
    fewest_needed = sorted(map(len, fitting_combos))[0]
    return len(list(filter(lambda x: len(x) == fewest_needed, fitting_combos)))
