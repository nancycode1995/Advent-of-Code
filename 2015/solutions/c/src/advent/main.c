#include <stdlib.h>
#include <stdio.h>

#include "solution.h"

int main(int argc, char **argv) {

    puts("Welcome to Nancy's Advent of Code 2015 solutions! :-)");

    size_t day = 0;
    size_t part = 0;

    if (argc > 3) {
        fprintf(stderr, "Usage: %s [day] [part]\n", argv[0]);
        return EXIT_FAILURE;
    }

    if (argc > 2) {
        part = atoi(argv[2]);
        if (part < 1 || part > 2) {
            fprintf(stderr, "There is no such part %zu!\n", part);
            return EXIT_FAILURE;
        }
    }

    if (argc > 1) {
        day = atoi(argv[1]);
        if (day < 1 || day > N_DAYS) {
            fprintf(stderr, "There is no such day %zu!\n", day);
            return EXIT_FAILURE;
        }
    }

    if (day) {
        day--;
        if (part == 1)
            solution_run_one(day);
        else if (part == 2)
            solution_run_two(day);
        else
            solution_run(day);
    } else
        for (size_t i = 0; i < N_DAYS; i++)
            solution_run(i);

    return EXIT_SUCCESS;
}
