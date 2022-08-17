import sys

import solutions

def run(day=None, part=None):
    print(f"Welcome to Nancy's Advent of Code 2015 solutions! :-)")
    day = int(day) if day else day
    if day and 1 <= day <= 25:
        solution = solutions.days[day - 1]
        if part == "1":
            solution.run_one()
        elif part == "2":
            solution.run_two()
        elif part == None:
            solution.run()
        else:
            sys.exit(f"There is no such part {part}!")
    elif day == None:
        for i, solution in enumerate(solutions.days):
            print(f"Day {i + 1}:")
            solution.run()
    else:
        sys.exit(f"There is no such day {day}!")

def main(cmd, *args):
    if len(args) > 2:
        sys.exit(f"Usage: {args[0]} [day] [part]")
    else:
        run(*args)

if __name__ == "__main__":
    main(*sys.argv)
