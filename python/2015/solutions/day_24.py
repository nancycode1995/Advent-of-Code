#!/usr/bin/env python3

from itertools import combinations, count

from solutions.solution import SolutionBase

def prod(values):
    product = 1
    for value in values:
        product *= value
    return product

def solution_into_n_parts(string, n):
    # The package weights
    weights = list(map(int, string.split()))

    # Total weight
    total = sum(weights)

    # Evenly divide
    group_sum = total // n

    # Find the possible groupings starting from lowest number of packagesthat add to group_sum
    for i in count(1):
        groups = list(filter(lambda group: sum(group) == group_sum, combinations(weights, i)))

        # We keep trying until we find the tying groups for lowest size
        if len(groups) > 0:

            # Find quantum entanglements
            quantum_entanglements = [prod(group) for group in groups]

            # Find the lowest quantum entanglement and return that as the answer
            return sorted(quantum_entanglements)[0]

class Solution(SolutionBase):
    def part_one(self):
        return solution_into_n_parts(self.input, 3)

    def part_two(self):
        return solution_into_n_parts(self.input, 4)

solution = Solution.instantiate(24)

if __name__ == "__main__":
    solution.run()
