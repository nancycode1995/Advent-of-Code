#!/usr/bin/env python3

from itertools import groupby

from advent import solution

def look_and_say(string, iterations=1):
    for i in range(iterations):
        print(f"Iteration {i}/{iterations} = {len(string)}")
        string = "".join([f"{len(list(group))}{key}" for key, group in groupby(string)])
    return string

@solution("10.txt", "Part 1")
def solve(string):
    return len(look_and_say(string, 40))

@solution("10.txt", "Part 2")
def solve(string):
    return len(look_and_say(string, 50))
