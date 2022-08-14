#!/usr/bin/env python3

from advent import solution

class Aunt:
    def __init__(self, name, **attributes):
        self.name = name
        self.attributes = attributes

    @classmethod
    def from_string(cls, string):
        name, attributes_string = string.split(": ", maxsplit=1)
        attribute_strings = attributes_string.split(", ")
        pairs = [string.split(": ") for string in attribute_strings]
        attributes = {attribute:int(value) for attribute, value in pairs}
        return cls(name, **attributes)

    def matches(self, **attributes):
        for attribute, value in attributes.items():
            if attribute in self.attributes and value != self.attributes[attribute]:
                return False
        return True

    def matches_2(self, **attributes):
        for attribute, value in attributes.items():
            if attribute in self.attributes:
                if attribute in ("cats", "trees"):
                    if value >= self.attributes[attribute]:
                        return False
                elif attribute in ("pomeranians", "goldfish"):
                    if value <= self.attributes[attribute]:
                        return False
                elif value != self.attributes[attribute]:
                    return False
        return True

def parse_aunts(string):
    return list(map(Aunt.from_string, string.split("\n")))

attributes = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
        }

@solution("16.txt", "Part 1")
def solve(string):
    aunts = parse_aunts(string)
    return next(filter(lambda aunt: aunt.matches(**attributes), aunts)).name

@solution("16.txt", "Part 2")
def solve(string):
    aunts = parse_aunts(string)
    return next(filter(lambda aunt: aunt.matches_2(**attributes), aunts)).name
