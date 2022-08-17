#!/usr/bin/env python3

import sys

import day_1
import day_2
import day_3
import day_4
import day_5
import day_6
import day_7
import day_8
import day_9
import day_10
import day_11
import day_12
import day_13
import day_14
import day_15
import day_16
import day_17
import day_18
import day_19
import day_20
import day_21
import day_22
import day_23
import day_24
import day_25

days = [
        day_1.solution,
        day_2.solution,
        day_3.solution,
        day_4.solution,
        day_5.solution,
        day_6.solution,
        day_7.solution,
        day_8.solution,
        day_9.solution,
        day_10.solution,
        day_11.solution,
        day_12.solution,
        day_13.solution,
        day_14.solution,
        day_15.solution,
        day_16.solution,
        day_17.solution,
        day_18.solution,
        day_19.solution,
        day_20.solution,
        day_21.solution,
        day_22.solution,
        day_23.solution,
        day_24.solution,
        day_25.solution,
        ]


def run(day=None, part=None):
    print(f"Welcome to Nancy's Advent of Code 2015 solutions! :-)")
    day = int(day) if day else day
    if day and 1 <= day <= 25:
        solution = days[day - 1]
        if part == "1":
            solution.run_one()
        elif part == "2":
            solution.run_two()
        elif part == None:
            solution.run()
        else:
            sys.exit(f"There is no such part {part}!")
    elif day == None:
        for i, solution in enumerate(days):
            print(f"Day {i + 1}:")
            solution.run()
    else:
        sys.exit(f"There is no such day {day}!")

def main(cmd, *args):
    if len(args) > 2:
        sys.exit(f"Usage: {cmd} [day] [part]")
    else:
        run(*args)

if __name__ == "__main__":
    main(*sys.argv)
