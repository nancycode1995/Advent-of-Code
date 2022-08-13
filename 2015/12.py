#!/usr/bin/env python3

import json

from advent import solution

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

@solution("12.txt", "Part 1")
def solve(string):
    data = json.loads(string)
    return count(data)

@solution("12.txt", "Part 2")
def solve(string):
    data = json.loads(string)
    return count(data, "red")
