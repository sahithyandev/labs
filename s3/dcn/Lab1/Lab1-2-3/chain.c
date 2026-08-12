#include <stdio.h>
#include <stdlib.h> // includes malloc(), free(), realloc()
#include <string.h> // includes memcpy()

#include "chain.h" // do not modify this file

// put your function prototypes for additional helper functions below:

int power(int base, int exp)
{
    if (exp == 0)
    {
        return 1;
    }

    if (exp & 1)
    {
        return base * power(base, exp - 1);
    }
    int half = power(base, exp / 2);
    return half * half;
}

// implementation
matrix *create_matrix(int num_rows, int num_cols)
{
    matrix *mat = malloc(sizeof(matrix));
    if (mat == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }

    mat->num_rows = num_rows;
    mat->num_cols = num_cols;
    mat->data = malloc(num_rows * sizeof(int *));
    if (mat->data == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }

    for (int i = 0; i < num_rows; i++)
    {
        mat->data[i] = malloc(num_cols * sizeof(int));
        if (mat->data[i] == NULL)
        {
            fprintf(stderr, "Memory allocation failed\n");
            exit(1);
        }
        memset(mat->data[i], 0, num_cols * sizeof(int)); // Initialize to zero
    }

    return mat;
}

void add_row(matrix *mat, int *row)
{
    mat->num_rows += 1;
    int **new_data = realloc(mat->data, mat->num_rows * sizeof(int *));
    if (new_data == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }
    new_data[mat->num_rows - 1] = malloc(mat->num_cols * sizeof(int));
    if (new_data[mat->num_rows - 1] == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }
    memcpy(new_data[mat->num_rows - 1], row, mat->num_cols * sizeof(int));
    mat->data = new_data;
}

void add_col(matrix *mat, int *col)
{
    mat->num_cols += 1;
    for (int i = 0; i < mat->num_rows; i++)
    {
        int *new_row = realloc(mat->data[i], mat->num_cols * sizeof(int));
        if (new_row == NULL)
        {
            fprintf(stderr, "Memory allocation failed\n");
            exit(1);
        }
        new_row[mat->num_cols - 1] = col[i];
        mat->data[i] = new_row;
    }
}

void increment(matrix *mat, int num)
{
    for (int i = 0; i < mat->num_rows; i++)
    {
        for (int j = 0; j < mat->num_cols; j++)
        {
            mat->data[i][j] += num;
        }
    }
}

void scalar_multiply(matrix *mat, int num)
{
    for (int i = 0; i < mat->num_rows; i++)
    {
        for (int j = 0; j < mat->num_cols; j++)
        {
            mat->data[i][j] *= num;
        }
    }
}

void scalar_divide(matrix *mat, int num)
{
    for (int i = 0; i < mat->num_rows; i++)
    {
        for (int j = 0; j < mat->num_cols; j++)
        {
            mat->data[i][j] /= num;
        }
    }
}

void scalar_power(matrix *mat, int num)
{
    for (int i = 0; i < mat->num_rows; i++)
    {
        for (int j = 0; j < mat->num_cols; j++)
        {
            mat->data[i][j] = power(mat->data[i][j], num);
        }
    }
}

void delete_matrix(matrix *mat)
{
    if (mat == NULL)
        return;

    for (int i = 0; i < mat->num_rows; i++)
    {
        free(mat->data[i]);
    }
    free(mat->data);
    free(mat);
}

/*
    DO NOT MODIFY BELOW
*/
// print out matrix in row-major order
// elements in the same row are space-separated
// each row starts in a new line
void print_matrix(matrix *mat)
{
    int row_idx, col_idx;
    for (row_idx = 0; row_idx < mat->num_rows; ++row_idx)
    {
        for (col_idx = 0; col_idx < mat->num_cols; ++col_idx)
        {
            if (col_idx == mat->num_cols - 1)
            {
                printf("%d\n", mat->data[row_idx][col_idx]);
            }
            else
            {
                printf("%d ", mat->data[row_idx][col_idx]);
            }
        }
    }
}

// Add the rest of the functions needed for the chain below
