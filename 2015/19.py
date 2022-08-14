#!/usr/bin/env python3

from random import shuffle

from advent import solution

def patch(string, substring, index, length):
    """Replace a portion of a string."""
    return string[:index] + substring + string[index + length:]

def indices(string, substring):
    """Yield the indices of all occurences of the substring within the string."""

    for i in range(len(string)):
        if string[i:].startswith(substring):
            yield i

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
    replacements_string, molecule = string.split("\n\n")
    replacements = [tuple(s.strip() for s in string.split("=>")) for string in replacements_string.split("\n")]

    def try_random_search(molecule, target="e"):
        """Attempt a random path."""
        steps = 0
        while molecule != "e":
            old = molecule
            shuffle(replacements)
            for left, right in replacements:
                if right in molecule:
                    molecule = molecule.replace(right, left)
                    steps += 1
            if old == molecule:
                # Dead end
                return -1
        # Success in this number of steps
        return steps

    # Try several random paths and pick the lowest
    # (Relying on probability that the answer will be correct)
    paths = [try_random_search(molecule) for i in range(1000000)]
    filtered = list(filter(lambda x: x != -1, paths))
    return min(*filtered)
