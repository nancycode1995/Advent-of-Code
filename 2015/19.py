#!/usr/bin/env python3

from advent import solution

def patch(string, substring, index, length):
    """Replace a portion of a string."""
    return string[:index] + substring + string[index + length:]

def indices(string, substring):
    """Yield the indices of all occurences of the substring within the string."""

    position = 0
    while (index := string[position:].find(substring)) != -1:
        yield position + index
        position += index + 1

@solution("19.txt", "Part 1")
def solve(string):
    replacements_string, molecule = string.split("\n\n")
    replacements = [tuple(s.strip() for s in string.split("=>")) for string in replacements_string.split("\n")]
    molecules = set()
    for source, replacement in replacements:
        for index in indices(molecule, source):
            replaced = patch(molecule, replacement, index, len(source))
            molecules.add(replaced)
    return len(molecules)

@solution("19.txt", "Part 2")
def solve(string):
    replacements_string, target = string.split("\n\n")
    replacements = [tuple(s.strip() for s in string.split("=>")) for string in replacements_string.split("\n")]

    def fewest_steps(molecule):
        if molecule == target:
            return 0
        if len(molecule) > len(target):
            return None
        def tree():
            for source, replacement in replacements:
                for index in indices(molecule, source):
                    replaced = patch(molecule, replacement, index, len(source))
                    yield fewest_steps(replaced)
        return min(filter(lambda x: x != None, tree()))

    return fewest_steps("e")
