#!/usr/bin/env python3

from advent import solution

def consume_run(rest, run=""):
    while run == "" or rest.startswith(run[0]):
        run += rest[0]
        rest = rest[1:]
    return run, rest

def look_and_say(rest, consumed=""):
    while rest:
        run, rest = consume_run(rest)
        consumed += f"{len(run)}{run[0]}"
    return consumed

def do_iterations(string, iterations: int):
    for i in range(iterations):
        print(f"Iteration {i + 1}/{iterations}")
        string = look_and_say(string)
    return len(string)

@solution("10.txt", "Part 1")
def solve(string):
    return do_iterations(string, 40)

@solution("10.txt", "Part 2")
def solve(string):
    return do_iterations(string, 50)
