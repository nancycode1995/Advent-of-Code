#!/usr/bin/env python3

from __future__ import annotations
from itertools import permutations

from solutions.solution import SolutionBase

class Place:
    def __init__(self, name: str, distances: dict):
        self.name = name
        self.distances = distances

    @property
    def places(self) -> set:
        """The set of places that can be traveled to from this place."""
        return self.distances.keys()

    def distance(self, place) -> int:
        """The distance from here to the given place."""
        return self.distances[place]

class Path:
    """A sequence of places arranged in the order that santa will traverse them."""
    def __init__(self, places, santa_map):
        self.places = places
        self.map = santa_map

    @property
    def distance(self):
        """The total distance of the path from start to finish."""
        places_a, places_b = self.places[:-1], self.places[1:]
        return sum(self.map.distance(a, b) for a, b in zip(places_a, places_b))

class Map:
    """Complete undirected graph of santa's destinations and the distances between every pair of places."""
    def __init__(self, places: set):
        self.places = {place.name for place in places}
        self._places = {place.name: place for place in places}

    def __getitem__(self, place: str):
        return self._places[place]

    def distance(self, a: str, b: str) -> int:
        """The distance between two places on the map."""
        return self[a].distance(b)

    @classmethod
    def from_string(cls, string: str):
        """Compile the string representation of a directory into a map object representation."""
        return Directory.from_string(string).to_map()

    @property
    def paths(self) -> list:
        """Return all possible paths."""
        return [Path(places, self) for places in permutations(self.places)]

    @property
    def shortest_path(self) -> Path:
        """Return the shortest path santa can travel on the map in order to reach every place exactly one time."""
        return sorted(self.paths, key=lambda path: path.distance)[0]

    @property
    def longest_path(self) -> Path:
        """Return the longest path santa can travel on the map in order to reach every place exactly one time."""
        return sorted(self.paths, key=lambda path: path.distance)[-1]

class Record:
    """A record of distance as it appears in input file."""
    def __init__(self, source: str, destination: str, distance: int):
        self.source = source
        self.destination = destination
        self.distance = distance

    @classmethod
    def from_string(cls, string: str):
        """Assemble a record object from a line in the input file."""
        source, _, destination, _, distance = string.split()
        return cls(source, destination, int(distance))

class Directory:
    """A list of records as they appear in the input file."""
    def __init__(self, records: list):
        self.records = records

    @classmethod
    def from_string(cls, string: str):
        """Assemble the string representation to object representation."""
        return cls([Record.from_string(line) for line in string.split("\n")])

    def to_map(self):
        """Compile directory into a map representation."""
        place_distances = {}
        def get_distances(place):
            if place not in place_distances:
                place_distances[place] = {}
            return place_distances[place]
        for record in self.records:
            distances_source = get_distances(record.source)
            distances_destination = get_distances(record.destination)
            distances_source[record.destination] = record.distance
            distances_destination[record.source] = record.distance
        return Map({Place(name, distances) for name, distances in place_distances.items()})

class Solution(SolutionBase):
    def part_one(self):
        return Map.from_string(self.input).shortest_path.distance

    def part_two(self):
        return Map.from_string(self.input).longest_path.distance

solution = Solution.instantiate(9)

if __name__ == "__main__":
    solution.run()
