#!/usr/bin/env python3

from abc import ABC, abstractmethod
from itertools import product, combinations

from advent import solution

class Item:
    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

    def __repr__(self):
        return f'Item("{self.name}")'

class Store:
    def __init__(self):
        self.weapons = [
                Item("Dagger",     8,  4, 0),
                Item("Shortsword", 10, 5, 0),
                Item("Warhammer",  25, 6, 0),
                Item("Longsword",  40, 7, 0),
                Item("Greataxe",   74, 8, 0),
                ]
        self.armor = [
                Item("Leather",    13,  0, 1),
                Item("Chainmail",  31,  0, 2),
                Item("Splintmail", 53,  0, 3),
                Item("Bandedmail", 75,  0, 4),
                Item("Platemail",  102, 0, 5),
                ]
        self.rings = [
                Item("Damage +1",  25,  1, 1),
                Item("Damage +2",  50,  2, 0),
                Item("Damage +3",  100, 3, 0),
                Item("Defense +1", 20,  0, 1),
                Item("Defense +2", 40,  0, 2),
                Item("Defense +3", 80,  0, 3),
                ]

class Character(ABC):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    @property
    @abstractmethod
    def damage(self):
        """Total damage score."""
        ...

    @property
    @abstractmethod
    def armor(self):
        """Total armor score."""
        ...

    def attack(self, opponent) -> (int, int):
        """Attack an opponent character and return the amount of damage inflicted and remaining hp of opponent."""
        damage = max(1, self.damage - opponent.armor)
        opponent.hp -= damage
        return damage, opponent.hp

class Player(Character):
    def __init__(self, hp=100, items=None):
        super().__init__("Player", hp)
        self.items = items or []

    @property
    def damage(self):
        """Total damage score as determined by possessed items."""
        return sum(item.damage for item in self.items)

    @property
    def armor(self):
        """Total armor score as determined by possessed items."""
        return sum(item.armor for item in self.items)

class Boss(Character):
    def __init__(self, hp, damage, armor):
        super().__init__("Boss", hp)
        self._damage = damage
        self._armor = armor

    @property
    def damage(self):
        return self._damage

    @property
    def armor(self):
        return self._armor

class Game:
    def __init__(self, properties, items=None):
        self.player = Player(items=items)
        self.boss = Boss(properties["Hit Points"], properties["Damage"], properties["Armor"])

    def turn(self):
        """Do one round of turns and return the winner if someone dies."""
        # Player's turn
        damage, hp = self.player.attack(self.boss)
        print(f"The player deals {damage}; the boss goes down to {hp} hit points.")
        if hp <= 0:
            return self.player

        # Boss's turn
        damage, hp = self.boss.attack(self.player)
        print(f"The boss deals {damage}; the player goes down to {hp} hit points.")
        if hp <= 0:
            return self.boss

    def play(self):
        """Play the game until the end and return whether player wins."""
        print(f"Game begins.")
        items_string = ", ".join(item.name for item in self.player.items)
        print(f"Player equipped items: {items_string}!")
        print(f"Total cost: {self.spent}")
        print(f"Player has {self.player.hp} hit points, {self.player.damage} damage points, and {self.player.armor} armor points.")
        print(f"Boss has {self.boss.hp} hit points, {self.boss.damage} damage points, and {self.boss.armor} armor points.")
        while True:
            if winner := self.turn():
                print(f"{winner.name} wins!")
                return winner == self.player

    @property
    def spent(self):
        """The amount of money that the player has spent."""
        return sum(item.cost for item in self.player.items)

# Store singleton
store = Store()

@solution("21.txt", "Part 1")
def solve(string):
    # Load the given boss stats
    properties = {k:int(v) for k, v in [line.split(": ") for line in string.split("\n")]}

    def games():
        """Yield all possible games within buying constraints."""

        # Constraints:
        # Must purchase 1 weapon
        # Must purchase either 0 or 1 armor
        # Must purchase 0, 1, or 2 rings
        n_items_per_category_range = range(1, 2), range(0, 2), range(0, 3)
        categories = store.weapons, store.armor, store.rings
        for n_items_per_category in product(*n_items_per_category_range):
            for items_per_category in product(*(combinations(category, n_items) for n_items, category in zip(n_items_per_category, categories))):
                items = sum(map(list, items_per_category), [])
                yield Game(properties, items)

    # Play all games to find winning games
    winning = filter(lambda game: game.play(), games())

    # Sort the winning games by amount of gold spent
    ranking = sorted(winning, key=lambda game: game.spent)

    # Answer is least amount of gold
    # Replay the game of the answer for fun
    game = Game(properties, ranking[0].player.items)
    game.play()
    return game.spent
