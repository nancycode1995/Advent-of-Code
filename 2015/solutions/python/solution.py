from abc import ABC, abstractmethod
import sys

def read_file(path):
    try:
        with open(path) as stream:
            return stream.read().strip()
    except FileNotFoundError:
        sys.exit(f'Unable to open file "{path}"!')

class SolutionBase:
    def __init__(self, input, answer_one, answer_two):
        self.input = input
        self.answer_one = answer_one
        self.answer_two = answer_two

    @classmethod
    def from_paths(cls, path_input, path_answer_one, path_answer_two):
        return cls(read_file(path_input), read_file(path_answer_one), read_file(path_answer_two))

    @classmethod
    def instantiate(cls, day):
        path_input = f"../../inputs/{day}.txt"
        path_answer_one = f"../../answers/{day}.1.txt"
        path_answer_two = f"../../answers/{day}.2.txt"
        return cls.from_paths(path_input, path_answer_one, path_answer_two)

    @abstractmethod
    def part_one(self):
        """Return the answer to part one of this day's solution."""
        ...

    @abstractmethod
    def part_two(self):
        """Return the answer to part two of this day's solution."""
        ...

    def test_one(self):
        """Solve part one and test the result against the known correct answer."""
        assert(str(self.part_one()) == self.answer_one)
        return self.answer_one

    def test_two(self):
        """Solve part two and test the result against the known correct answer."""
        assert(str(self.part_one()) == self.answer_one)
        return self.answer_two

    def test(self):
        """Solve both parts and test the results against the known correct answwers."""
        return self.test_one(), self.test_two()

    def run_one(self):
        """Perform a test of part one and print the result to console."""
        print("Solving part one...")
        answer_one = str(self.part_one())
        if answer_one == self.answer_one:
            print(f"Result: {answer_one} (CORRECT)")
        else:
            print(f"Result: {answer_one} (INCORRECT; should be {self.answer_one})")

    def run_two(self):
        """Perform a test of part two and print the result to console."""
        print("Solving part two...")
        answer_two = str(self.part_two())
        if answer_two == self.answer_two:
            print(f"Result: {answer_two} (CORRECT)")
        else:
            print(f"Result: {answer_two} (INCORRECT; should be {self.answer_two})")

    def run(self):
        """Perform a test of both parts and print the results to console."""
        self.run_one()
        self.run_two()
