#!/usr/bin/env python3

from functools import cache

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

    def replace(molecule):
        """Yield all possible BACKWARDS replacements given a molecule."""
        for source, replacement in replacements:
            for index in indices(molecule, replacement):
                yield patch(molecule, source, index, len(replacement))

    @cache
    def search(molecule, target="e", depth=0):
        """Perform backwards depth-first brute-force search."""
        # If we found the target, cease recursion and return depth
        if molecule == target:
            return depth
        # Get the next level of the tree
        # Filter out dead ends
        generation = [search(replaced, target, depth + 1) for replaced in replace(molecule)]
        filtered = list(filter(lambda x: x != -1, generation))
        # As we are searching for the shortest path,
        # take the minimum steps
        if filtered:
            return filtered[0] if len(filtered) == 1 else min(*filtered)
        # If we arrive at a dead end (no results), cease recursion and return -1 to signify target not found
        else:
            return -1

    return search(molecule)
