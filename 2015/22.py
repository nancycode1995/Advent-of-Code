#!/usr/bin/env python3

from abc import ABC, abstractmethod
from itertools import product, combinations, permutations

from advent import solution

class Spell:
    def __init__(self, name, cost, damage, armor, hp, mana, effect):
        self.name = name     # Name of spell
        self.cost = cost     # Mana cost of spell
        self.damage = damage # Damage score for attack
        self.armor = armor   # Armor score for defense
        self.hp = hp         # Heals this many hit points
        self.mana = mana     # Gives you this much mana per turn
        self.effect = effect # Number of turns during which it remains active

    def __repr__(self):
        return f'Spell("{self.name}")'

    def cast(self, character, opponent):
        """Apply cast effect."""
        character.mana -= self.cost
        if self.effect == 0:
            opponent.hp -= self.damage
        character.hp += self.hp
        return Effect(self)

    def turn(self, character, opponent):
        """Apply turn effects."""
        opponent.hp -= self.damage
        character.mana += self.mana

class Effect:
    def __init__(self, spell):
        self.spell = spell
        self.timer = spell.effect

    def turn(self, character, opponent):
        if self.timer > 0:
            self.spell.turn(character, opponent)
            self.timer -= 1
            return self.timer

spells = [
        Spell("Magic Missile", 53,  4, 0, 0, 0,   0),
        Spell("Drain",         73,  2, 0, 2, 0,   0),
        Spell("Shield",        113, 0, 7, 0, 0,   6),
        Spell("Poison",        173, 3, 0, 0, 0,   6),
        Spell("Recharge",      229, 0, 0, 0, 191, 5),
        ]

class Character(ABC):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    @abstractmethod
    def inflict(self, damage) -> (int, int):
        """Inflict damage onto this character and return the amount actualy inflicted and remaining hit points."""
        ...

    @abstractmethod
    def turn_passive(self, opponent):
        """This happens every turn, regardless of whose turn it is."""
        ...

    @abstractmethod
    def turn(self, opponent):
        """It is this character's turn."""
        ...

class Player(Character):
    def __init__(self, hp=50, mana=500, spells=spells, turns=None):
        super().__init__("Player", hp)
        self.spells = spells or []
        self.effects = []
        self.turns = turns or iter()
        self.spent = 0

    def inflict(self, damage) -> (int, int):
        armor = sum(effect.armor for effect in self.effects)
        effective = max(1, damage - armor)
        self.hp -= effective
        return effective, self.hp

    def turn_passive(self, opponent):
        self.effects = list(filter(lambda effect: effect.timer > 0, self.effects))
        for effect in self.effects:
            effect.turn(self, opponent)

    def turn(self, opponent) -> (int, int):
        spell = next(self.turns)
        if spell not in self.effects:
            self.spent += spell.cost
            self.effects.append(spell.cast(self, opponent))

class Boss(Character):
    def __init__(self, hp, damage):
        super().__init__("Boss", hp)
        self.damage = damage

    def inflict(self, damage) -> (int, int):
        self.hp -= damage
        return damage, self.hp

    def turn_passive(self, opponent):
        pass

    def turn(self, opponent) -> (int, int):
        return opponent.inflict(self.damage)

class Game:
    def __init__(self, properties, turns):
        self.player = Player(turns=turns)
        self.boss = Boss(properties["Hit Points"], properties["Damage"])

    def turn(self):
        """Do one round of turns and return the winner if someone dies."""
        for character, opponent in permutations([self.player, self.boss]):
            self.character.turn_passive(self.opponent)
            self.opponent.turn_passive(self.character)
            damage, hp = self.character.turn(self.opponent)
            if hp <= 0:
                return self.character

    def play(self):
        """Play the game until the end and return whether player wins."""
        print(f"Game begins.")
        while True:
            if winner := self.turn():
                print(f"{winner.name} wins!")
                return winner == self.player

    @property
    def spent(self):
        return self.player.spent

def games(properties):
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

@solution("21.txt", "Part 1")
def solve(string):
    # Load the given boss stats
    properties = {k:int(v) for k, v in [line.split(": ") for line in string.split("\n")]}

#    # Sort the games by cost
#    sorted_games = sorted(games(properties), key=lambda game: game.spent)
#
#    # Play through all games in order until the first success
#    for game in sorted_games:
#        if game.play():
#            return game.spent
