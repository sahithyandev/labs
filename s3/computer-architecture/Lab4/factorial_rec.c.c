#include <stdio.h>

void print_int(int num);

int n = 7;

int main(int argc, char **argv)
{
    int x = 1;
    for (int i = n; i > 1; i--) {
        x *= i;
    }
    print_int(x);

    return 0;
}

void print_int(int num)
{
    /* Print the num variable */
    asm("mv a0, %0"::"r"(num)); /* Store the value of num in a0 register */
    asm("li a7, 1"); /* ecall 1 = print_int */
    asm("ecall");
    
    /* Print a new line */
    asm("li a0, 10"); /* Store the new line character in a0 register (ASCII(\n) = 10) */
    asm("li a7, 11"); /* ecall 11 = print_char */
    asm("ecall");
    
    return;
}