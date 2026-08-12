#include <stdio.h>

int arr_sum(int arr[], int index, int arr_size);
void print_int(int num);

int main(int argc, char **argv)
{
    int a = 5;
    int b = 10;

    int c = a * b;
    printf("%d\n",c);
    
    c = b / a;
    print_int(c);
    
    int arr_size = 5;
    int arr [5] = {78, 58, 36, 96, 23};
    int sum = arr_sum(arr, 0, arr_size);
    printf("%d\n", sum);
    print_int(sum);

    return 0;
}

int arr_sum(int arr[], int index, int arr_size) {
    if (index >= arr_size)
        return 0;
        
    return arr[index] + arr_sum(arr, index + 1, arr_size);
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