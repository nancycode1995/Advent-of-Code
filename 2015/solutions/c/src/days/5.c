#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#include "solution.h"

#define MAX_LINES 1000

static char *lines[MAX_LINES];

static char *skip_replace_character(char *string, char character, char replace) {
    char c;
    while ((c = *(string++)))
        if (*string == character)
            return *string = replace, string + 1;
    return string - 1;
}

static void read_lines(char *string, char **lines, size_t *n_lines) {
    for (*n_lines = 0; *string; (*n_lines)++)
        string = lines[*n_lines] = skip_replace_character(string, '\n', '\0');
}

static bool has_three_vowels(char *string) {
    size_t n_vowels = 0;
    for (; *string; string++)
        n_vowels += *string == 'a'
                 || *string == 'e'
                 || *string == 'i'
                 || *string == 'o'
                 || *string == 'u';
    return n_vowels >= 3;
}

static bool has_double_letter(char *string) {
    while (*(++string))
        if (*string == *(string - 1))
            return true;
    return false;
}

static size_t count(char *haystack, char *needle) {
    size_t size_needle = strlen(needle);
    size_t n = 0;
    while ((haystack = strstr(haystack, needle))) {
        n++;
        /* non overlapping */
        haystack += size_needle;
    }
    return n;
}

static bool has_double_pair(char *string) {
    char pair[3];
    pair[2] = '\0';
    char *p = string;
    while (*(++p)) {
        pair[0] = *(p - 1);
        pair[1] = *p;
        if (count(string, pair) >= 2)
            return true;
    }
    return false;
}

static bool has_double_letter_with_gap(char *string) {
    string++;
    while (*(++string))
        if (*string == *(string - 2))
            return true;
    return false;
}

static bool has_no_bad_strings(char *string) {
    return strstr(string, "ab") == NULL
        && strstr(string, "cd") == NULL
        && strstr(string, "xy") == NULL
        && strstr(string, "pq") == NULL;
}

void solution_day_5_part_1(char *input, char *output) {
    char *buffer = malloc(sizeof(char) * MAX_LINES * 64);
    strcpy(buffer, input);
    size_t n_lines = 0;
    read_lines(buffer, lines, &n_lines);
    size_t n_nice = 0;
    char *line = *lines;
    for (int i = 0; i < n_lines; line = lines[i++]) {
        n_nice += has_three_vowels(line)
               && has_double_letter(line)
               && has_no_bad_strings(line);
    }
    sprintf(output, "%zu", n_nice);
    free(buffer);
}

void solution_day_5_part_2(char *input, char *output) {
    char *buffer = malloc(sizeof(char) * MAX_LINES * 64);
    strcpy(buffer, input);
    size_t n_lines = 0;
    read_lines(buffer, lines, &n_lines);
    size_t n_nice = 0;
    char *line = *lines;
    for (int i = 0; i < n_lines; line = lines[i++]) {
        n_nice += has_double_letter_with_gap(line)
               && has_double_pair(line);
    }
    sprintf(output, "%zu", n_nice);
    free(buffer);
}
