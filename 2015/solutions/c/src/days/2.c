#include <stdio.h>

#include "solution.h"

#define MAX_PRESENTS 1000

typedef struct {
    int length, width, height;
} present_t;

int required_paper(present_t *present) {
    int a = present->length * present->width;
    int b = present->length * present->height;
    int c = present->width * present->height;
    int sum = a + b + c;
    int smallest = a < b ? a : b;
    smallest = c < smallest ? c : smallest;
    return 2 * sum + smallest;
}

int required_ribbon(present_t *present) {
    int a = present->length + present->width;
    int b = present->length + present->height;
    int c = present->width + present->height;
    int smallest = a < b ? a : b;
    int volume = present->length * present->width * present->height;
    smallest = c < smallest ? c : smallest;
    return 2 * smallest + volume;
}

char *skip_character(char *string, char character) {
    char c;
    while ((c = *(string++)))
        if (*string == character)
            return string + 1;
    return NULL;
}

char *parse_present(present_t *present, char *string) {
    present->length = atoi(string);
    string = skip_character(string, 'x');
    present->width = atoi(string);
    string = skip_character(string, 'x');
    present->height = atoi(string);
    return skip_character(string, '\n');
}

size_t parse_presents(present_t *presents, char *string) {
    size_t i = 0;
    while (*string)
        string = parse_present(&presents[i++], string);
    return i;
}

void solution_day_2_part_1(char *input, char *output) {
    present_t presents[MAX_PRESENTS];
    size_t n_presents = parse_presents(presents, input);
    int sum = 0;
    for (int i = 0; i < n_presents; i++)
        sum += required_paper(&presents[i]);
    sprintf(output, "%d", sum);
}

void solution_day_2_part_2(char *input, char *output) {
    present_t presents[MAX_PRESENTS];
    size_t n_presents = parse_presents(presents, input);
    int sum = 0;
    for (int i = 0; i < n_presents; i++)
        sum += required_ribbon(&presents[i]);
    sprintf(output, "%d", sum);
}
