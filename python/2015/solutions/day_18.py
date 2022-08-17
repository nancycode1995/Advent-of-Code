#!/usr/bin/env python3

from itertools import product

from solutions.solution import SolutionBase

def animate(grid, width):
    def animate_light(i, state):
        x_, y_ = divmod(i, width)
        num_neighbors = 0
        for x, y in product(range(x_ - 1, x_ + 2), range(y_ - 1, y_ + 2)):
            if x == x_ and y == y_:
                continue
            if x in range(width) and y in range(width):
                j = y + x * width
                if grid[j] == "#":
                    num_neighbors += 1
        if state == "#":
            return "#" if num_neighbors == 2 or num_neighbors == 3 else "."
        else:
            return "#" if num_neighbors == 3 else "."
    return list(animate_light(i, state) for i, state in enumerate(grid))

def print_grid(grid, width):
    for i in range(len(grid) // width):
        print("".join(grid[i * width:i * width + width]))
    print()

class Solution(SolutionBase):
    def part_one(self):
        width = len(self.input.strip().split()[0])
        grid = "".join(self.input.strip().split())
        #print_grid(grid, width)
        for i in range(100):
            grid = animate(grid, width)
            #print_grid(grid, width)
        return grid.count("#")

    def part_two(self):
        width = len(self.input.strip().split()[0])
        def patch(grid):
            grid[0] = "#"
            grid[width - 1] = "#"
            grid[-1] = "#"
            grid[-width] = "#"
        grid = list("".join(self.input.strip().split()))
        patch(grid)
    #    print_grid(grid, width)
        for i in range(100):
            grid = animate(grid, width)
            patch(grid)
    #        print_grid(grid, width)
        return grid.count("#")

solution = Solution.instantiate(18)

if __name__ == "__main__":
    solution.run()
