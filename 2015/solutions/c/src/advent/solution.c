#include <stdio.h>

#include "solution.h"

#define SIZE_OUTPUT 256

solution_t *solutions[N_DAYS][2];

void read_input(size_t day, char *buffer) {
    // TODO: compute input file path for this day
    // TODO: read the contents of the file into buffer
    // TODO: return success status
}

void check(size_t day, size_t part, char *output) {
    // TODO: compute answer file path for this part and this day
    // TODO: read contents of file
    // TODO: compare given answer with contents of file
    // TODO: include indication of correctness in message
    // TODO: free resources
    printf("Result: %s\n", output);
}

void run(size_t day, size_t part) {
    char *input, *output;

    printf("Solving day %zu, part %zu...\n", day + 1, part + 1);

    /* get the solution function for this part of this day */
    solution_t *solution = solutions[day][part];

    /* load the puzzle input and allocate an output buffer */
    // TODO: handle errors */
    read_input(day, input);
    output = malloc(sizeof(char) * SIZE_OUTPUT);

    /* perform the calculation */
    solution(input, output);

    /* compare the result with the known correct answer */
    check(day, part, output);

    /* free resources */
    free(input);
    free(output);
}

void solution_run(size_t day) {
    solution_run_one(day);
    solution_run_two(day);
}

void solution_run_one(size_t day) {
    run(day, 0);
}

void solution_run_two(size_t day) {
    run(day, 1);
}
