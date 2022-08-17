#!/usr/bin/env python3

from itertools import permutations

from solutions.solution import SolutionBase

def parse_rule(string):
    person, string = string.split(maxsplit=1)
    rule_type, string = string[:10], string[10:]
    amount, string = string.split(maxsplit=1)
    string = string[35:]
    other_person = string[:-1]
    amount = int(amount)
    gain = amount if rule_type == "would gain" else -amount
    return (person, other_person), gain

def parse_rules(string):
    rules = list(map(parse_rule, string.split("\n")))
    people = set(rule[0][0] for rule in rules)
    pairs = {pair:gain for pair, gain in rules}
    return people, pairs

def net_gain(arrangement, pairs):
    def gain(person):
        position = arrangement.index(person)
        left = arrangement[position - 1]
        right = arrangement[(position + 1) % len(arrangement)]
        left_pair = person, left
        right_pair = person, right
        left_gain = pairs[person, left] if left_pair in pairs else 0
        right_gain = pairs[person, right] if right_pair in pairs else 0
        return left_gain + right_gain
    return sum(map(gain, arrangement))

def find_solution(people, pairs):
    arrangements = list(permutations(people))
    return sorted(net_gain(arrangement, pairs) for arrangement in arrangements)[-1]

class Solution(SolutionBase):
    def part_one(self):
        return find_solution(*parse_rules(self.input))

    def part_two(self):
        people, pairs = parse_rules(self.input)
        people.add("Me")
        return find_solution(people, pairs)

solution = Solution.instantiate(13)

if __name__ == "__main__":
    solution.run()
