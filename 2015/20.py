#!/usr/bin/env python3

from advent import solution

@solution("20.txt", "Part 1")
def solve(string):
    min_presents = int(string) // 10
    print("First elf visits all the houses...")
    houses = [1 for i in range(min_presents)]
    for i in range(2, min_presents):
        print(f"Elf {i} of {min_presents} ({i/min_presents*100:.2}%) visits all the houses...")
        for j in range(i, min_presents, i):
            houses[j] += i
    print("Finding first house...")
    return next(filter(lambda x: x[1] >= min_presents, enumerate(houses)))

@solution("20.txt", "Part 2")
def solve(string):
    min_presents = int(string)
    print("First elf visits all the houses...")
    houses = [11 for i in range(min_presents // 11)]
    num_houses = len(houses)
    for i in range(2, num_houses):
        print(f"Elf {i} of {num_houses} ({i*1000//num_houses/10}%) visits all the houses...")
        j = i
        p = i * 11
        for k in range(50):
            if j >= num_houses:
                break
            houses[j] += p
            j += i
    print("Finding first house...")
    return next(filter(lambda x: x[1] >= min_presents, enumerate(houses)))
