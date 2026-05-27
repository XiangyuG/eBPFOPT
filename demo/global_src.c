#include <stdio.h>

int g = 0;

int func(int x) {
    g = g + x;
    return g;
}