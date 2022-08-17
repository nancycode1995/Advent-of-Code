#!/usr/bin/env python3

from itertools import cycle

from solution import SolutionBase

directions = {
        "<": (-1, 0),
        ">": (1, 0),
        "^": (0, -1),
        "v": (0, 1),
        }

def tuple_add(a: tuple, b: tuple) -> tuple:
    """Create a new tuple whose elements are the sums of the corresponding elements in two given tuples."""
    return tuple(x + y for x, y in zip(a, b))

class Santa:
    def __init__(self, deliveries, position=(0, 0)):
        """Takes a pointer to the dictionary used to track deliveries."""
        self.position = position
        self.deliveries = deliveries

        # deliver initial present
        self.deliver()

    def deliver(self):
        """Deliver a present to the house at the current location."""
        if self.position not in self.deliveries:
            self.deliveries[self.position] = 1
        else:
            self.deliveries[self.position] += 1

    def move(self, character):
        """Move in some direction designated by a character and deliver a present at the new position."""
        self.position = tuple_add(self.position, directions[character])
        self.deliver()

class Solution(SolutionBase):
    def part_one(self):
        deliveries = {}
        santa = Santa(deliveries)
        for character in self.input:
            santa.move(character)
        return len(deliveries)

    def part_two(self):
        deliveries = {}
        santa = Santa(deliveries)
        robo_santa = Santa(deliveries)
        for character, receiver in zip(self.input, cycle([santa, robo_santa])):
            receiver.move(character)
        return len(deliveries)

solution = Solution.instantiate(3)

if __name__ == "__main__":
    solution.run()
