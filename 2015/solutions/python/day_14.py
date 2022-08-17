#!/usr/bin/env python3

from solution import SolutionBase

class Reindeer:
    def __init__(self, name, speed, fly_duration, rest_duration):
        self.name = name
        self.speed = speed
        self.fly_duration = fly_duration
        self.rest_duration = rest_duration

    @property
    def cycle_duration(self):
        return self.fly_duration + self.rest_duration

    @property
    def cycle_distance(self):
        return self.speed * self.fly_duration

    @classmethod
    def from_string(cls, string):
        name, _, _, speed, _, _, fly_duration, _, _, _, _, _, _, rest_duration, _ = string.split()
        return cls(name, int(speed), int(fly_duration), int(rest_duration))

    def distance_after(self, seconds):
        """Return the distance travels after a given number of seconds."""
        # number of complete fly, rest cycles that have occurred
        cycles, remaining = divmod(seconds, self.cycle_duration)
        distance = cycles * self.cycle_distance

        # account also for partial cycle distance
        return distance + min(self.fly_duration, remaining) * self.speed

def parse_reindeer(string):
    return list(map(Reindeer.from_string, string.split("\n")))

def race(reindeer, seconds):
    return {deer: deer.distance_after(seconds) for deer in reindeer}

class Solution(SolutionBase):
    def part_one(self):
        reindeer = parse_reindeer(self.input)
        results = race(reindeer, 2503)
        return sorted(results.values())[-1]

    def part_two(self):
        reindeer = parse_reindeer(self.input)
        points = {deer.name:0 for deer in reindeer}
        for i in range(2503):
            state = sorted(race(reindeer, i + 1).items(), key=lambda item: item[1])
            lead, distance = state[-1]
            leading = list(filter(lambda deer: deer[1] == distance, state))
            for deer, distance in leading:
                points[deer.name] += 1
        return sorted(points.values())[-1]

solution = Solution.instantiate(14)

if __name__ == "__main__":
    solution.run()
