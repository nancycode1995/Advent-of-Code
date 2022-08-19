#include <stdio.h>
#include <string.h>

#include "solution.h"

#define BASE 1000

int presents[BASE * BASE];

void solution_day_3_part_1(char *input, char *output) {
    int position = BASE * BASE / 2;
    memset(presents, 0, sizeof(int) * BASE * BASE);
    presents[position] += 1;
    char c;
    while ((c = *(input++))) {
        switch (c) {
            case '<':
                position -= 1;
                break;
            case '>':
                position += 1;
                break;
            case '^':
                position -= BASE;
                break;
            case 'v':
                position += BASE;
                break;
        }
        presents[position] += 1;
    }
    int count = 0;
    for (int i = 0; i < BASE * BASE; i++)
        count += presents[i] > 0;
    sprintf(output, "%d", count);
}

void solution_day_3_part_2(char *input, char *output) {
    int position_santa = BASE * BASE / 2;
    int position_robo = BASE * BASE / 2;
    memset(presents, 0, sizeof(int) * BASE * BASE);
    presents[position_santa] += 2;
    int i = 0;
    char c;
    while ((c = *(input++))) {
        int *p = i++ % 2 ? &position_santa : &position_robo;
        switch (c) {
            case '<':
                *p -= 1;
                break;
            case '>':
                *p += 1;
                break;
            case '^':
                *p -= BASE;
                break;
            case 'v':
                *p += BASE;
                break;
        }
        presents[*p] += 1;
    }
    int count = 0;
    for (int i = 0; i < BASE * BASE; i++)
        count += presents[i] > 0;
    sprintf(output, "%d", count);
}
