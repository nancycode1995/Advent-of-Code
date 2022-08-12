import sys

def solution(path_input, prompt="Solution"):
    """Return a decorator function which calls a given solution function with the string contents of the file at path_input."""

    def decorator(function_solve):
        """Call the given solution function with the string contents of the file at path_input."""

        try:
            with open(path_input) as stream:
                contents = stream.read().strip()
                solution = function_solve(contents)
                print(f"{prompt}: {solution}")
        except FileNotFoundError:
            sys.exit(f'Unable to open file "{path_input}"!')

    return decorator
