#!/usr/bin/env python3

from solution import SolutionBase

def is_vowel(character):
    return character.lower() in "aeiou"

def subsequent_pairs(string):
    return zip(string[:-1], string[1:])

def subsequent_separated_pairs(string):
    return zip(string[:-2], string[2:])

def has_three_vowels(string):
    vowels = filter(is_vowel, string)
    return len(list(vowels)) >= 3

def has_double_letter(string):
    return any(a == b for a, b in subsequent_pairs(string))

def has_no_bad_strings(string):
    bad_strings = "ab", "cd", "pq", "xy"
    return not any(bad_string in string for bad_string in bad_strings)

def has_double_pair(string):
    return any(string.count(f"{a}{b}") > 1 for a, b in subsequent_pairs(string))

def has_double_letter_with_one_character_gap(string):
    return any(a == b for a, b in subsequent_separated_pairs(string))

def get_nice_strings(strings, conditions):
    is_nice = lambda string: all(condition(string) for condition in conditions)
    return filter(is_nice, strings)

class Solution(SolutionBase):
    def part_one(self):
        conditions = has_three_vowels, has_double_letter, has_no_bad_strings
        return len(list(get_nice_strings(self.input.split(), conditions)))

    def part_two(self):
        conditions = has_double_pair, has_double_letter_with_one_character_gap
        return len(list(get_nice_strings(self.input.split(), conditions)))

solution = Solution.instantiate(5)

if __name__ == "__main__":
    solution.run()
