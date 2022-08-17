#!/usr/bin/env python3

from itertools import product

from advent import solution

@solution("25.txt", "Part 1")
def solve(string):
    # Read the input for the coordinates
    row_string, string = string.split("row")[1].split(", column")
    row = int(row_string)
    column = int(string.split(".")[0])

    # Convert coordinates on the diagonal infinite paper to index
    def get_index(row, column):
        index = 1
        for i in range(row + column - 1):
            index += i
        return index + column - 1

    # Compute the next code
    def next_code(code):
        return code * 252533 % 33554393

    # Iterate the algorithm to find the nth code
    code = 20151125 # The initial code
    for i in range(get_index(row, column) - 1):
        code = next_code(code)

    # The answer
    return code