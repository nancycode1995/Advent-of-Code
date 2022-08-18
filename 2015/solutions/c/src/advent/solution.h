#ifndef SOLUTION_H
#define SOLUTION_H

#include <stdlib.h>

#define N_DAYS 25

/* solution function for calculating the answer to a part */
typedef void solution_t(char *input, char *output);

/* lookup table of solution functions for each day */
extern solution_t *solutions[N_DAYS][2];

/* run both parts of a solution given the day index */
void solution_run(size_t day);

/* run either specific part of a given day */
void solution_run_one(size_t day);
void solution_run_two(size_t day);

#endif /* SOLUTION_H */
