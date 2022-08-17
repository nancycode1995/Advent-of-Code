#!/usr/bin/env python3

from abc import ABC, abstractmethod
from itertools import permutations
from copy import deepcopy

from solution import SolutionBase

quiet = True

class InvalidMoveException(Exception):
    pass

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

    def cast(self, character, opponent) -> (int, int):
        """Apply cast effect."""
        damage = self.damage if self.effect == 0 else 0
        character.mana -= self.cost
        opponent.hp -= damage
        character.hp += self.hp
        return damage, opponent.hp, Effect(self.name)

    def turn(self, character, opponent) -> (int, int):
        """Apply turn effects."""
        opponent.hp -= self.damage
        character.mana += self.mana
        return self.damage, self.mana

Spell.spells = {spell.name:spell for spell in [
    Spell("Magic Missile", 53,  4, 0, 0, 0,   0),
    Spell("Drain",         73,  2, 0, 2, 0,   0),
    Spell("Shield",        113, 0, 7, 0, 0,   6),
    Spell("Poison",        173, 3, 0, 0, 0,   6),
    Spell("Recharge",      229, 0, 0, 0, 101, 5),
    ]}

class Effect:
    def __init__(self, spell: str):
        self.spell = spell
        self.timer = Spell.spells[spell].effect

    def turn(self, character, opponent):
        if self.timer > 0:
            spell = Spell.spells[self.spell]
            damage, mana = spell.turn(character, opponent)
            self.timer -= 1
            if not quiet:
                print(f"{spell.name} deals {damage} damage and gives {character.name} {mana} mana; its timer is now {self.timer}.")
            return self.timer

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
    def __init__(self, hp=50, mana=500):
        super().__init__("Player", hp)
        self.mana = mana
        self.effects = []
        self.spent = 0

    @property
    def armor(self) -> int:
        return sum(Spell.spells[effect.spell].armor for effect in self.effects)

    def inflict(self, damage) -> (int, int):
        effective = max(1, damage - self.armor)
        self.hp -= effective
        return effective, self.hp

    def turn_passive(self, opponent):
        for effect in self.effects:
            effect.turn(self, opponent)
        self.effects = list(filter(lambda effect: effect.timer > 0, self.effects))

    def turn(self, opponent, spell: str) -> (int, int):
        if spell not in [effect.spell for effect in self.effects]:
            spell = Spell.spells[spell]
            if spell.cost <= self.mana:
                self.spent += spell.cost
                damage, hp, effect = spell.cast(self, opponent)
                if not quiet:
                    string = f", dealing {damage} damage." if damage else "."
                    print(f"{self.name} casts {spell.name}{string}")
                if effect.timer > 0:
                    self.effects.append(effect)
                return damage, hp
            else:
                raise InvalidMoveException(f"Not enough mana to cast spell {spell.name}!")
        else:
            raise InvalidMoveException(f"Spell {spell} already in effect!")

class Boss(Character):
    def __init__(self, hp, damage):
        super().__init__("Boss", hp)
        self.damage = damage

    def inflict(self, damage) -> (int, int):
        self.hp -= damage
        return damage, self.hp

    def turn_passive(self, opponent):
        pass

    def turn(self, opponent, spell: str) -> (int, int):
        damage, hp = opponent.inflict(self.damage)
        if not quiet:
            print(f"{self.name} attacks for {damage} damage.")
        return damage, hp

class Game:
    def __init__(self, properties, player_turn_damage):
        self.player = Player()
        self.boss = Boss(properties["Hit Points"], properties["Damage"])
        self.player_turn_damage = player_turn_damage
        self.winner = None
        self.history = []

    def turn(self, spell: str):
        """Do one round of turns and return the winner if someone dies. Cast the given spell as the player's move."""

        if self.winner:
            #print("This game is already finished.")
            return self.winner

        self.history.append(spell)

        characters = self.player, self.boss
        for character, opponent in permutations(characters):
            if not quiet:
                print(f"\n-- {character.name} turn --")
                print(f"- {self.player.name} has {self.player.hp} hit points, {self.player.armor} armor, {self.player.mana} mana")
                print(f"- {self.boss.name} has {self.boss.hp} hit points")

            # Player turn damage for part 2
            if character == self.player:
                if self.player_turn_damage > 0:
                    if not quiet:
                        print(f"{self.player.name} takes {self.player_turn_damage} turn damage.")
                    self.player.hp -= self.player_turn_damage
                    if self.player.hp <= 0:
                        if not quiet:
                            print(f"{self.player.name} dies of turn damage!")
                        self.winner = self.boss
                        return self.winner

            character.turn_passive(opponent)
            opponent.turn_passive(character)
            if character.hp <= 0:
                self.winner = opponent
                return opponent
            damage, hp = character.turn(opponent, spell)
            if hp <= 0:
                self.winner = character
                return character

    def play(self, turns):
        """Play the game until the end and return whether player wins."""
        #print(f"Game begins.")
        while True:
            if winner := self.turn(next(turns)):
                #print(f"{winner.name} wins!")
                return winner == self.player

    @property
    def spent(self):
        return self.player.spent

    def clone(self):
        """Return a deep copy of the current game state (for backtracking purposes)."""
        return deepcopy(self)

def test_game(properties):
    """Run the example scenario to test that everything works properly."""
    turns = "Recharge", "Shield", "Drain", "Poison", "Magic Missile"
    game = Game(properties)
    game.player.hp = 10
    game.player.mana = 250
    game.boss.hp = 14
    game.boss.damage = 8
    game.play(iter(turns))

def play(string, player_turn_damage=0):
    # Load the given boss stats
    properties = {k:int(v) for k, v in [line.split(": ") for line in string.split("\n")]}

    # The initial game based on given starting conditions
    game = Game(properties, player_turn_damage)

    # Initial moves (for starting mid search if I have to stop the script before finding solution)
    initial_moves = []

    # All possible spells in order from least expensive
    spells = [spell.name for spell in sorted(Spell.spells.values(), key=lambda spell: spell.cost)]

    def find_lowest_cost_game(initial, moves=[], best=None) -> Game:
        """Use back tracking depth first search to explore all possible games starting from lowest cost until the first winning game is found. If initial moves are given, start on that branch first."""

        #if quiet and 0 < len(initial.history) < 3:
        #    s = f"({best.spent}) " if best else ""
        #    print(s + " -> ".join(initial.history), "..." if len(initial.history) == 2 else "")

        # If this branch has already spent more than the best winning game, then this branch cannot yield a better result, so stop here!
        if best and best.spent <= initial.spent:
            return best

        # If the game is already finished, then cease recursion
        if initial.winner:
            if initial.winner == initial.player:
                # This is the first winning game on this branch
                #print(f"Winning game: {' -> '.join(initial.history)}")
                return initial
            else:
                # This is a losing game, no winning games on this branch
                return best

        # Constrain attempted spells to given initial moves
        if moves:
            available_spells = spells[spells.index(moves[0]):]
        else:
            available_spells = spells

        # Try all possible next moves
        for spell in available_spells:

            # Clone the given game state in case we need to backtrack
            game = initial.clone()

            try:
                # Attempt this move
                game.turn(spell)

                # Update the best game
                best = find_lowest_cost_game(game, moves[1:], best)

            # The attempted move may be invalid, in which case we skip it
            except InvalidMoveException as exception:
                if not quiet:
                    print(exception)

            # Otherwise, try the next game
            continue

        # Return the best game we found
        return best

    # Find the lowest cost game and the total cost of that game
    return find_lowest_cost_game(game, initial_moves).spent

class Solution(SolutionBase):
    def part_one(self):
        return play(self.input)

    def part_two(self):
        return play(self.input, 1)

solution = Solution.instantiate(22)

if __name__ == "__main__":
    solution.run()
