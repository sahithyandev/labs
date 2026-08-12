#include <stdio.h>

#define N 8

int MaxVector(int A[], int size)
{
    int max = 0, ind = 0, j;
    for (j = 0; j < size; j++)
    {
        if (A[j] > max)
        {
            max = A[j];
            ind = j;
        }
    }
    A[ind] = 0;
    return (max);
}

int SortVector(int A[], int B[], int size)
{
    int max, j;
    for (j = 0; j < size; j++)
    {
        max = MaxVector(A, size);
        B[j] = max;
    }
    return (0);
}

int main(void)
{
    int A[N] = {7, 3, 25, 4, 75, 2, 1, 1}, B[N];
    SortVector(A, B, N);
    return (0);
}
