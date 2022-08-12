#!/usr/bin/env python3

from itertools import count
from hashlib import md5

from advent import solution

def find_hash(secret, match_function):
    inputs = (f"{secret}{x}".encode("ascii") for x in count())
    hashed = (md5(hash_input).hexdigest() for hash_input in inputs)
    pairs = zip(count(), hashed)
    valid = filter(lambda x: match_function(x[1]), pairs)
    return next(valid)[0]

@solution("4.txt", "Part 1")
def solve(string):
    matches = lambda hashed: str(hashed).startswith("00000")
    return find_hash(string, matches)

@solution("4.txt", "Part 2")
def solve(string):
    matches = lambda hashed: str(hashed).startswith("000000")
    return find_hash(string, matches)
