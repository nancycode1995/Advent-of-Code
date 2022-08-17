#!/usr/bin/env python3

from solution import SolutionBase

class Solution(SolutionBase):
    def part_one(self):
        min_presents = int(self.input) // 10
        #print("First elf visits all the houses...")
        houses = [1 for i in range(min_presents)]
        for i in range(2, min_presents):
            #print(f"Elf {i} of {min_presents} ({i/min_presents*100:.2}%) visits all the houses...")
            for j in range(i, min_presents, i):
                houses[j] += i
        #print("Finding first house...")
        return next(filter(lambda x: x[1] >= min_presents, enumerate(houses)))[0]

    def part_two(self):
        min_presents = int(self.input)
        #print("First elf visits all the houses...")
        houses = [11 for i in range(min_presents // 11)]
        num_houses = len(houses)
        for i in range(2, num_houses):
            #print(f"Elf {i} of {num_houses} ({i*1000//num_houses/10}%) visits all the houses...")
            j = i
            p = i * 11
            for k in range(50):
                if j >= num_houses:
                    break
                houses[j] += p
                j += i
        #print("Finding first house...")
        return next(filter(lambda x: x[1] >= min_presents, enumerate(houses)))[0]

solution = Solution.instantiate(20)

if __name__ == "__main__":
    solution.run()
