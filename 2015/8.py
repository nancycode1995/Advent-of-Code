#!/usr/bin/env python3

from advent import solution

def encode(string):
    def encode_character(character):
        if character == "\\":
            return "\\\\"
        if character == "\"":
            return "\\\""
        else:
            return character
    return '"' + "".join(list(map(encode_character, string))) + '"'

@solution("8.txt", "Part 1")
def solve(string):
    # a totally cheaty and non production safe solution!
    literals = string.split()
    strings = list(map(eval, literals))
    lengths_literals = list(map(len, literals))
    lengths_strings = list(map(len, strings))
    total_literals = sum(lengths_literals)
    total_strings = sum(lengths_strings)
    return total_literals - total_strings

@solution("8.txt", "Part 2")
def solve(string):
    literals = string.split()
    representations = list(map(encode, literals))
    lengths_literals = list(map(len, literals))
    lengths_representations = list(map(len, representations))
    total_literals = sum(lengths_literals)
    total_representations = sum(lengths_representations)
    return total_representations - total_literals
