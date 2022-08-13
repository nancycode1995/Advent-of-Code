#!/usr/bin/env python3

from itertools import groupby

from advent import solution

radix = ord("z") - ord("a") + 1 # aka base 26

def decode(password: str) -> int:
    """Decode the password into number form."""
    digits = [ord(letter) - ord("a") for letter in password[::-1]]
    return sum(radix ** i * digit for i, digit in enumerate(digits))

def encode(password: int, length: int = None) -> str:
    """Encode a number into password form."""
    string = ""
    while len(string) < 8 if length != None else password > 0:
        password, digit = divmod(password, radix)
        string += chr(digit + ord("a"))
    return string[::-1]

def increment(password: str) -> str:
    """Increment the password using santa's method."""
    return encode(decode(password) + 1, 8)

def has_correct_length(password: str) -> bool:
    return len(password) == 8

def get_straights(string: str, length: int) -> list:
    return [string[i:i + length] for i in range(len(string) - length + 1)]

def is_increasing_straight(straight: str) -> bool:
    values = list(map(ord, straight))
    translated = [value - i for i, value in enumerate(values)]
    return len(set(translated)) <= 1

def has_increasing_straight(password: str) -> bool:
    return len(list(filter(is_increasing_straight, get_straights(password, 3)))) > 0

def does_not_have_invalid_letters(password: str) -> bool:
    invalid_letters = "iol"
    for letter in invalid_letters:
        if letter in password:
            return False
    return True

def has_pairs(password: str) -> bool:
    groups = groupby(password)
    groups_of_more_than_one = list(filter(lambda group: len(list(group[1])) > 1, groups))
    return len(groups_of_more_than_one) >= 2

def is_valid(password: str) -> bool:
    """Whether a password string passes all security requirements."""
    conditions = has_correct_length, has_increasing_straight, does_not_have_invalid_letters, has_pairs
    return all(function(password) for function in conditions)

def find_next_password(password: str) -> str:
    password = increment(password)
    while not is_valid(password):
        password = increment(password)
    return password

@solution("11.txt", "Part 1")
def solve(password):
    return find_next_password(password)

@solution("11.txt", "Part 2")
def solve(password):
    return find_next_password(find_next_password(password))
