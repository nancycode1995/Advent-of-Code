#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

#include "solution.h"

#define MAX_INSTRUCTIONS 1000

typedef enum {
    INSTRUCTION_TYPE_ENABLE,
    INSTRUCTION_TYPE_DISABLE,
    INSTRUCTION_TYPE_TOGGLE,
    N_INSTRUCTION_TYPE
} instruction_type_t;

typedef struct {
    size_t x, y;
} position_t;

typedef struct {
    instruction_type_t type;
    position_t a, b;
} instruction_t;

void run_instruction_enable(position_t a, position_t b, int *lights, size_t lights_width, int part) {
    for (size_t i = a.x; i <= b.x; i++)
        for (size_t j = a.y; j <= b.y; j++)
            if (part == 0)
                lights[i + j * lights_width] = true;
            else
                lights[i + j * lights_width]++;
}

void run_instruction_disable(position_t a, position_t b, int *lights, size_t lights_width, int part) {
    for (size_t i = a.x; i <= b.x; i++)
        for (size_t j = a.y; j <= b.y; j++)
            if (part == 0)
                lights[i + j * lights_width] = false;
            else
                lights[i + j * lights_width] = fmax(0, lights[i + j * lights_width] - 1);
}

void run_instruction_toggle(position_t a, position_t b, int *lights, size_t lights_width, int part) {
    for (size_t i = a.x; i <= b.x; i++)
        for (size_t j = a.y; j <= b.y; j++)
            if (part == 0)
                lights[i + j * lights_width] = !lights[i + j * lights_width];
            else
                lights[i + j * lights_width] += 2;
}

typedef void run_instruction_function_t(position_t, position_t, int *, size_t, int);

run_instruction_function_t *run_instruction_functions[] = {
    run_instruction_enable,
    run_instruction_disable,
    run_instruction_toggle
};

void run_instruction(instruction_t instruction, int *lights, size_t lights_width, int part) {
    run_instruction_functions[instruction.type](instruction.a, instruction.b, lights, lights_width, part);
}

void run_program(instruction_t *instructions, size_t n_instructions, int *lights, size_t lights_width, int part) {
    for (size_t i = 0; i < n_instructions; i++)
        run_instruction(instructions[i], lights, lights_width, part);
}

bool expect(char **stream, char *string) {
    char *start = *stream;
    while (*string) {
        if (*string != **stream) {
            *stream = start;
            return false;
        }
        (*stream)++;
        string++;
    }
    return true;
}

size_t consume_until(char **stream, char c) {
    size_t i = 0;
    while (**stream != c) {
        (*stream)++;
        i++;
    }
    return i;
}

size_t consume_until_whitespace_or_null(char **stream) {
    size_t i = 0;
    while (!isspace((int) (**stream)) && **stream != '\0') {
        (*stream)++;
        i++;
    }
    return i;
}

bool parse_position(char **stream, position_t *position) {
    char string_1[64];
    char string_2[64];
    char *string_1_source = *stream;
    size_t string_1_length = consume_until(stream, ',');
    (*stream)++;
    char *string_2_source = *stream;
    size_t string_2_length = consume_until_whitespace_or_null(stream);
    strncpy(string_1, string_1_source, string_1_length);
    string_1[string_1_length] = '\0';
    strncpy(string_2, string_2_source, string_2_length);
    string_2[string_2_length] = '\0';
    position->x = atoi(string_1);
    position->y = atoi(string_2);
    return true;
}

bool parse_instruction(char **stream, instruction_t *instruction) {
    if (expect(stream, "turn on ")) {
        instruction->type = INSTRUCTION_TYPE_ENABLE;
    } else if (expect(stream, "turn off ")) {
        instruction->type = INSTRUCTION_TYPE_DISABLE;
    } else if (expect(stream, "toggle ")) {
        instruction->type = INSTRUCTION_TYPE_TOGGLE;
    } else return false;
    parse_position(stream, &instruction->a);
    expect(stream, " through ");
    parse_position(stream, &instruction->b);
    expect(stream, "\n");
    return true;
}

instruction_t *create_program_from_string(char *input, size_t *n_instructions) {
    instruction_t *instructions = malloc(sizeof(instruction_t) * MAX_INSTRUCTIONS);
    *n_instructions = 0;
    while (parse_instruction(&input, &instructions[*n_instructions]))
        (*n_instructions)++;
    return instructions;
}

void solution_day_6_part_1(char *input, char *output) {
    int *lights = malloc(sizeof(int) * 1000 * 1000);
    size_t n_instructions;
    instruction_t *instructions = create_program_from_string(input, &n_instructions);
    run_program(instructions, n_instructions, lights, 1000, 0);
    free(instructions);
    size_t n_lit = 0;
    for (size_t i = 0; i < 1000 * 1000; i++)
        n_lit += lights[i] ? 1 : 0;
    sprintf(output, "%zu", n_lit);
}

void solution_day_6_part_2(char *input, char *output) {
    int *lights = malloc(sizeof(int) * 1000 * 1000);
    size_t n_instructions;
    instruction_t *instructions = create_program_from_string(input, &n_instructions);
    run_program(instructions, n_instructions, lights, 1000, 1);
    free(instructions);
    int n_lit = 0;
    for (size_t i = 0; i < 1000 * 1000; i++)
        n_lit += lights[i];
    sprintf(output, "%d", n_lit);
}
