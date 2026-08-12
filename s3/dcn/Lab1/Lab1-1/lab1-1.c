// general purpose standard C lib
#include <stdio.h>
#include <stdlib.h> // stdlib includes malloc() and free()
#include <string.h>

// user-defined header files
#include "node.h"

// macros

#define INSERT_BEFORE 1
#define INSERT_AFTER 2
#define DELETE_NODE 3
#define DELETE_LIST 4

#define MAX_WORD_COUNT 100
#define MAX_WORD_SIZE 20
#define WORD_SEPARATOR (",")
#define LIST_INPUT_LINE_MAX_SIZE (MAX_WORD_COUNT * MAX_WORD_SIZE + MAX_WORD_COUNT - 1)

#define MAX_COMMAND_ARGS_COUNT 4
#define MAX_COMMAND_ARG_SIZE 20
#define COMMAND_INPUT_LINE_MAX_SIZE (MAX_COMMAND_ARGS_COUNT * MAX_COMMAND_ARG_SIZE + MAX_COMMAND_ARGS_COUNT - 1)
#define COMMAND_ARG_SEPARATOR (" ")

// function prototypes
void print_list(list *lst);
void run(list *lst);

void get_list_input(char **words, int *words_count)
{
    char line[LIST_INPUT_LINE_MAX_SIZE];

    fgets(line, LIST_INPUT_LINE_MAX_SIZE, stdin);

    line[strcspn(line, "\n")] = '\0'; // remove trailing newline
    char *token = strtok(line, WORD_SEPARATOR);
    int count = 0;
    while (token != NULL && count < MAX_WORD_COUNT)
    {
        words[count] = malloc((strlen(token) + 1) * sizeof(char));
        strcpy(words[count], token);
        count++;
        token = strtok(NULL, WORD_SEPARATOR);
    }

    *words_count = count;
}

void get_command_input(char **command_args, int *command_args_count)
{
    char line[COMMAND_INPUT_LINE_MAX_SIZE];

    fgets(line, COMMAND_INPUT_LINE_MAX_SIZE, stdin);

    line[strcspn(line, "\n")] = '\0'; // remove trailing newline
    char *token = strtok(line, COMMAND_ARG_SEPARATOR);
    int count = 0;
    while (token != NULL && count < MAX_COMMAND_ARGS_COUNT)
    {
        command_args[count] = malloc((strlen(token) + 1) * sizeof(char));
        strcpy(command_args[count], token);
        count++;
        token = strtok(NULL, COMMAND_ARG_SEPARATOR);
    }

    *command_args_count = count;
}

int main()
{
    list *lst = (list *)malloc(sizeof(list));
    lst->head = NULL;
    run(lst);
    print_list(lst);
    free(lst);
    return 0;
}

// parse the input
void run(list *lst)
{
    char **words = malloc(MAX_WORD_COUNT * sizeof(char *));
    int words_count = 0;
    get_list_input(words, &words_count);

    for (int i = 0; i < words_count; i++)
    {
        insert_node_before(lst, i, words[i]);
    }

    while (1)
    {
        char **command_args = malloc(MAX_COMMAND_ARGS_COUNT * sizeof(char *));
        int command_args_count = 0;

        get_command_input(command_args, &command_args_count);

        if (command_args_count == 0 || command_args_count == 1)
        {
            free(command_args);
            break;
        }

        switch (atoi(command_args[0]))
        {
        case INSERT_BEFORE:
            insert_node_before(lst, atoi(command_args[1]), command_args[2]);
            break;
        case INSERT_AFTER:
            insert_node_after(lst, atoi(command_args[1]), command_args[2]);
            break;
        case DELETE_NODE:
            delete_node(lst, atoi(command_args[1]));
            break;
        case DELETE_LIST:
            delete_list(lst);
            break;
        }
    }
}

// Print the list contents
void print_list(list *lst)
{

    if (lst->head == NULL)
    {
        printf("List is empty\n");
        return;
    }

    char *sentence = list_to_sentence(lst);
    if (sentence != NULL)
    {
        printf("%s\n", sentence);
        free(sentence);
    }
}
