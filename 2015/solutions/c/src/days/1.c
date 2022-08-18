#include <stdio.h>

#include "solution.h"

void solution_day_1_part_1(char *input, char *output) {
    int sum = 0;
    char character;
    while ((character = *(input++)))
        sum += character == '(' ? 1 : -1;
    sprintf(output, "%d", sum);
}

void solution_day_1_part_2(char *input, char *output) {
    int sum = 0;
    int i;
    char character;
    for (i = 0; (character = *(input++)) && sum >= 0; i++)
        sum += character == '(' ? 1 : -1;
    sprintf(output, "%d", i);
}
