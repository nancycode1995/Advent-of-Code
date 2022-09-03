#include <stdio.h>
#include <string.h>
#include <ctype.h>

#include "solution.h"
#include "../days/solution.h"

#define SIZE_OUTPUT 256

solution_t *solutions[N_DAYS][2] = {
    {solution_day_1_part_1,  solution_day_1_part_2},
    {solution_day_2_part_1,  solution_day_2_part_2},
    {solution_day_3_part_1,  solution_day_3_part_2},
    {solution_day_4_part_1,  solution_day_4_part_2},
    {solution_day_5_part_1,  solution_day_5_part_2},
    {solution_day_6_part_1,  solution_day_6_part_2},
    {solution_day_7_part_1,  solution_day_7_part_2},
    {solution_day_8_part_1,  solution_day_8_part_2},
    {solution_day_9_part_1,  solution_day_9_part_2},
    {solution_day_10_part_1, solution_day_10_part_2},
    {solution_day_11_part_1, solution_day_11_part_2},
    {solution_day_12_part_1, solution_day_12_part_2},
    {solution_day_13_part_1, solution_day_13_part_2},
    {solution_day_14_part_1, solution_day_14_part_2},
    {solution_day_15_part_1, solution_day_15_part_2},
    {solution_day_16_part_1, solution_day_16_part_2},
    {solution_day_17_part_1, solution_day_17_part_2},
    {solution_day_18_part_1, solution_day_18_part_2},
    {solution_day_19_part_1, solution_day_19_part_2},
    {solution_day_20_part_1, solution_day_20_part_2},
    {solution_day_21_part_1, solution_day_21_part_2},
    {solution_day_22_part_1, solution_day_22_part_2},
    {solution_day_23_part_1, solution_day_23_part_2},
    {solution_day_24_part_1, solution_day_24_part_2},
    {solution_day_25_part_1, solution_day_25_part_2},
};

char *read_file(char *path) {
    FILE *stream;
    size_t size_buffer;
    char *buffer;
    if (!(stream = fopen(path, "r"))) {
        fprintf(stderr, "Unable to open file at \"%s\"!\n", path);
        exit(EXIT_FAILURE);
    }
    fseek(stream, 0, SEEK_END);
    size_buffer = ftell(stream);
    fseek(stream, 0, SEEK_SET);
    if (!(buffer = malloc(sizeof(char) * (size_buffer + 1)))) {
        fprintf(stderr, "Unable to allocate memory!\n");
        exit(EXIT_FAILURE);
    }
    fread(buffer, sizeof(char), size_buffer, stream);
    buffer[size_buffer] = '\0';
    /* trim trailing whitespace */
    for (char *p = buffer + size_buffer - 1; isspace((int) *p); p--)
        *p = '\0';
    fclose(stream);
    return buffer;
}

char *read_input(size_t day) {
    char path[128];
    sprintf(path, "../../inputs/%zu.txt", day + 1);
    return read_file(path);
}

char *read_answer(size_t day, size_t part) {
    char path[128];
    sprintf(path, "../../answers/%zu.%zu.txt", day + 1, part + 1);
    return read_file(path);
}

void check(size_t day, size_t part, char *output) {
    /* load the answer for given day and part */
    char *answer = read_answer(day, part);

    /* compare and print results */
    printf("Result: %s ", output);
    if (strcmp(output, answer) == 0)
        printf("(CORRECT)\n");
    else
        printf("(INCORRECT; should be %s)\n", answer);

    /* free resources */
    free(answer);
}

void run(size_t day, size_t part) {
    char *input;
    char output[SIZE_OUTPUT];

    printf("Solving day %zu, part %zu... ", day + 1, part + 1);

    /* get the solution function for this part of this day */
    solution_t *solution = solutions[day][part];

    /* load the puzzle input and allocate an output buffer */
    input = read_input(day);

    /* perform the calculation */
    solution(input, output);

    /* compare the result with the known correct answer */
    check(day, part, output);

    /* free resources */
    free(input);
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
