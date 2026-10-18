//
// Program Vulnerabilities Part 2
// Canary, Bounds checking, Tagging
//
// Build: gcc -fno-stack-protector -o main main.c
// Run:   ./main [1-3]
// No arguments will run all 3 techniques

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//
// 1. Canary
//
// A fixed value after the buffer. If it changes, there was an overflow.

struct Frame {
    char buffer[8];
    int canary;
};

// No canary
void copyWithoutCanary(const char *input) {
    struct Frame f;
    memcpy(f.buffer, input, strlen(input) + 1);
    printf("Copied, nothing checked\n");
}

// With canary
void copyWithCanary(const char *input) {
    struct Frame f;
    f.canary = 12345;
    memcpy(f.buffer, input, strlen(input) + 1);
    if (f.canary != 12345)
        printf("Canary changed, overflow detected\n");
    else
        printf("Canary fine\n");
}

//
// 2. Bounds checking
//
// Check the index before using it.

int getValue(int *array, int size, int index) {
    if (index < 0 || index >= size) {
        printf("Index %d is out of bounds\n", index);
        return -1;
    }
    return array[index];
}

//
// 3. Tagging
//
// A tag says the type of the value.

struct Value {
    int isString;   // 1 = string, 0 = integer
    int number;
    char *text;
};

void printText(struct Value v) {
    if (!v.isString) {
        printf("Not a string, refusing to print\n");
        return;
    }
    printf("Text: %s\n", v.text);
}

void run(int which) {
    switch (which) {
        case 1:
            printf("--- Canary ---\n");
            copyWithoutCanary("AAAAAAAAAA");
            copyWithCanary("AAAAAAAAAA");
            break;
        case 2:
            printf("--- Bounds checking ---\n");
            int numbers[5] = {1, 2, 3, 4, 5};
            printf("numbers[2] = %d\n", getValue(numbers, 5, 2));
            printf("numbers[10] = %d\n", getValue(numbers, 5, 10));
            break;
        case 3:
            printf("--- Tagging ---\n");
            struct Value s = {1, 0, "hello"};
            struct Value n = {0, 12345, NULL};
            printText(s);
            printText(n);
            break;
        default:
            break;
    }
}



int main(int argc, char *argv[]) {
    int which = argc > 1 ? atoi(argv[1]) : 0;
    if (which == 0) {
        printf("argument is not provided. running all mitigation techniques\n");
        for (; which < 4; which++) {
            run(which);
        }
    } else {
        run(which);
    }

    return 0;
}
