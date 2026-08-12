// general purpose standard C lib
#include <stdio.h>
#include <stdlib.h> // stdlib includes malloc() and free()
#include <string.h>

// user-defined header files
#include "chain.h"

#define COMMAND_ADD_ROW 2
#define COMMAND_ADD_COLUMN 3
#define COMMAND_INCREMENT 4
#define COMMAND_SCALAR_MULTIPLY 5
#define COMMAND_SCALAR_DIVIDE 6
#define COMMAND_SCALAR_POWER 7
#define COMMAND_DELETE 8

// function prototypes
void print_chain(chain *chn);
void run(chain *chn);

int get_number_input()
{
    char line[20];
    fgets(line, sizeof(line), stdin);
    line[strcspn(line, "\n")] = '\0'; // remove trailing newline
    return atoi(line);
}

void get_numbers_input(int *numbers, int *count)
{
    char line[1000];
    *count = 0;

    fgets(line, sizeof(line), stdin);

    line[strcspn(line, "\n")] = '\0';

    char *token = strtok(line, " ");
    while (token != NULL && *count < 100)
    {
        numbers[*count] = atoi(token);
        (*count)++;
        token = strtok(NULL, " ");
    }
}

node *create_chain_node(matrix *mat)
{
    node *new_node = (node *)malloc(sizeof(node));
    if (new_node == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }
    new_node->mat = mat;
    new_node->prev = NULL;
    new_node->next = NULL;
    return new_node;
}

void duplicate_matrix(matrix *src, matrix **dest)
{
    *dest = create_matrix(src->num_rows, src->num_cols);
    for (int i = 0; i < src->num_rows; i++)
    {
        memcpy((*dest)->data[i], src->data[i], src->num_cols * sizeof(int));
    }
}

node *tail_of_chain(chain *chn)
{
    node *tail = chn->head;
    while (tail->next != NULL)
    {
        tail = tail->next;
    }
    return tail;
}

node *duplicate_tail_node(chain *chn)
{
    node *tail = tail_of_chain(chn);
    if (tail == NULL)
    {
        fprintf(stderr, "Error: Chain is empty.\n");
        exit(1);
    }
    node *new_node = (node *)malloc(sizeof(node));
    if (new_node == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }
    tail->next = new_node;
    tail->next->prev = tail;
    tail->next->next = NULL;
    duplicate_matrix(tail->mat, &tail->next->mat);
    return new_node;
}

int main()
{
    chain *chn = (chain *)malloc(sizeof(chain));
    chn->head = NULL;
    run(chn);
    print_chain(chn);
    free(chn);
    return 0;
}

// parse the input
void run(chain *chn)
{
    int num_rows = get_number_input();
    matrix *mat = create_matrix(0, 0);

    for (int i = 0; i < num_rows; i++)
    {
        int *row = malloc(100 * sizeof(int));
        if (row == NULL)
        {
            fprintf(stderr, "Memory allocation failed\n");
            exit(1);
        }
        int count = 0;

        get_numbers_input(row, &count);

        if (mat->num_cols == 0)
        {
            mat->num_cols = count;
        }
        else if (count != mat->num_cols)
        {
            fprintf(stderr, "Error: Row %d has a different number of columns than the first row.\n", i + 1);
            exit(1);
        }
        add_row(mat, row);
        free(row);
    }

    chn->head = create_chain_node(mat);

    while (1)
    {

        int commands[20];
        int count = 0;
        get_numbers_input(commands, &count);
        if (commands[0] == 0)
        {
            return;
        }

        node *new_node;
        new_node = duplicate_tail_node(chn);
        switch (commands[0])
        {
        case COMMAND_ADD_ROW:
            if (count < 2)
            {
                fprintf(stderr, "Error: Not enough arguments for COMMAND_ADD_ROW.\n");
                exit(1);
            }
            add_row(new_node->mat, &commands[1]);
            break;
        case COMMAND_ADD_COLUMN:
            if (count < 2)
            {
                fprintf(stderr, "Error: Not enough arguments for COMMAND_ADD_COLUMN.\n");
                exit(1);
            }
            add_col(new_node->mat, &commands[1]);
            break;
        case COMMAND_INCREMENT:
            if (count < 2)
            {
                fprintf(stderr, "Error: Not enough arguments for COMMAND_INCREMENT.\n");
                exit(1);
            }
            increment(new_node->mat, commands[1]);
            break;
        case COMMAND_SCALAR_MULTIPLY:
            if (count < 2)
            {
                fprintf(stderr, "Error: Not enough arguments for COMMAND_SCALAR_MULTIPLY.\n");
                exit(1);
            }
            scalar_multiply(new_node->mat, commands[1]);
            break;
        case COMMAND_SCALAR_DIVIDE:
            if (count < 2)
            {
                fprintf(stderr, "Error: Not enough arguments for COMMAND_SCALAR_DIVIDE.\n");
                exit(1);
            }
            scalar_divide(new_node->mat, commands[1]);
            break;
        case COMMAND_SCALAR_POWER:
            if (count < 2)
            {
                fprintf(stderr, "Error: Not enough arguments for COMMAND_SCALAR_POWER.\n");
                exit(1);
            }
            scalar_power(new_node->mat, commands[1]);
            break;
        }
    }
}

// Print the chain
void print_chain(chain *chn)
{
    node *current = chn->head;
    while (current != NULL)
    {
        print_matrix(current->mat);
        current = current->next;
        printf("\n");
    }
}
