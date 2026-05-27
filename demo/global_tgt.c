#include <stdio.h>

int g = 0;

int func(int x) {
    int next = g + x;
    g = next;
    return next;
}