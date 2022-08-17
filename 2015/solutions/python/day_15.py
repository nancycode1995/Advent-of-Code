#!/usr/bin/env python3

from itertools import product
from numpy import prod

from solution import SolutionBase

class Ingredient:
    def __init__(self, name, values):
        self.name = name
        self.values = values

    @classmethod
    def from_string(cls, string):
        name, properties_string = string.split(": ")
        property_strings = properties_string.split(", ")
        values = [int(property_string.split()[1]) for property_string in property_strings]
        return cls(name, values)

    def multiply(self, amount):
        return [value * amount for value in self.values]

def parse_ingredients(string):
    return list(map(Ingredient.from_string, string.split("\n")))

def score_recipe(ingredients: list, amounts: list):
    totals = [ingredient.multiply(amount) for ingredient, amount in zip(ingredients, amounts)]
    total_values = [max(0, sum(values)) for values in zip(*totals)]
    return prod(total_values[:-1])

def make_recipes(n, total=100):
    """Generate all possible recipes (amounts of ingredients)."""
    amounts = list(range(total + 1))
    return filter(lambda recipe: sum(recipe) == total, product(amounts, repeat=n))

def get_calories(ingredients, recipe):
    return sum([ingredient.values[-1] * amount for ingredient, amount in zip(ingredients, recipe)])

class Solution(SolutionBase):
    def part_one(self):
        ingredients = parse_ingredients(self.input)
        recipes = make_recipes(len(ingredients))
        winner = sorted(recipes, key=lambda recipe: score_recipe(ingredients, recipe))[-1]
        return score_recipe(ingredients, winner)

    def part_two(self):
        ingredients = parse_ingredients(self.input)
        #print("Making recipes...")
        recipes = make_recipes(len(ingredients))
        #print("Finding 500 calorie recipes...")
        calorie_fixed_recipes = list(filter(lambda recipe: get_calories(ingredients, recipe) == 500, recipes))
        #print("Finding the best one...")
        winner = sorted(calorie_fixed_recipes, key=lambda recipe: score_recipe(ingredients, recipe))[-1]
        return score_recipe(ingredients, winner)

solution = Solution.instantiate(15)

if __name__ == "__main__":
    solution.run()
