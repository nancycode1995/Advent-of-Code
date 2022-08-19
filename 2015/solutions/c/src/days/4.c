#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>

#include "solution.h"
#include "md5.h"

static void sprint_hash(char *output, uint8_t *hash) {
    for (int i = 0; i < 16; i++)
        sprintf(&output[i * 2], "%02x", (int) *(hash++));
}

static void solution(char *input, char *output, char *match) {
    uint8_t *hash;
    char string[64], hash_string[64];
    int i = 0;
    while (true) {
        sprintf(string, "%s%d", input, i++);
        /* TODO implement without reallocating buffer */
        hash = md5String(string);
        sprint_hash(hash_string, hash);
        free(hash);
        if (strncmp(hash_string, match, strlen(match)) == 0)
            break;
    }
    sprintf(output, "%d", i - 1);
}

void solution_day_4_part_1(char *input, char *output) {
    solution(input, output, "00000");
}

void solution_day_4_part_2(char *input, char *output) {
    solution(input, output, "000000");
}
