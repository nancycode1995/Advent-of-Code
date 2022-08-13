#!/usr/bin/env python3

from itertools import product
from numpy import prod

from advent import solution

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

@solution("15.txt", "Part 1")
def solve(string):
    ingredients = parse_ingredients(string)
    recipes = make_recipes(len(ingredients))
    winner = sorted(recipes, key=lambda recipe: score_recipe(ingredients, recipe))[-1]
    return winner, score_recipe(ingredients, winner)

@solution("15.txt", "Part 2")
def solve(string):
    ingredients = parse_ingredients(string)
    print("Making recipes...")
    recipes = make_recipes(len(ingredients))
    print("Finding 500 calorie recipes...")
    calorie_fixed_recipes = list(filter(lambda recipe: get_calories(ingredients, recipe) == 500, recipes))
    print("Finding the best one...")
    winner = sorted(calorie_fixed_recipes, key=lambda recipe: score_recipe(ingredients, recipe))[-1]
    return winner, score_recipe(ingredients, winner)
