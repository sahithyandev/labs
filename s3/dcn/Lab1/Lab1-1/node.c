// general purpose standard C lib
#include <stdio.h>
#include <stdlib.h> // includes malloc(),free()
#include <string.h> // includes strlen(), memcpy()
#include <ctype.h>	// includes toupper(), tolower()

// user-defined header files
#include "node.h" // do not modify this file

// put your function prototypes for additional helper functions below:
node *create_node(char *word)
{

	node *n = malloc(sizeof(node));
	if (n == NULL)
	{
		fprintf(stderr, "Memory allocation failed\n");
		exit(1);
	}
	n->word = word;
	n->prev = n;
	n->next = n;
	return n;
}

node *find_node_at(list *lst, int index)
{
	node *target_node = lst->head;
	while (index != 0)
	{
		if (target_node == NULL)
		{
			exit(2);
		}
		if (index > 0)
		{
			target_node = target_node->next;
			index -= 1;
		}
		else
		{
			target_node = target_node->prev;
			index += 1;
		}
	}
	return target_node;
}

size_t sentence_length_of_list(list *lst)
{
	size_t total_length = 0;
	node *current = lst->head;

	do
	{
		total_length += strlen(current->word) + 1;
		current = current->next;
	} while (current != lst->head);
	return total_length;
}

// implementation
void insert_node_before(list *lst, int index, char *word)
{
	if (lst->head == NULL)
	{
		lst->head = create_node(word);
		return;
	}

	node *target_node = find_node_at(lst, index);
	node *inserted_node = create_node(word);

	inserted_node->next = target_node;
	inserted_node->prev = target_node->prev;

	target_node->prev->next = inserted_node;
	target_node->prev = inserted_node;
	return;
}

void insert_node_after(list *lst, int index, char *word)
{
	return insert_node_before(lst, index + 1, word);
}

char *list_to_sentence(list *lst)
{
	if (lst->head == NULL)
	{
		return NULL;
	}

	node *current = lst->head;
	size_t total_length = sentence_length_of_list(lst);

	char *sentence = malloc(total_length);
	if (sentence == NULL)
	{
		fprintf(stderr, "Memory allocation failed\n");
		exit(1);
	}

	current = lst->head;
	size_t offset = 0;
	do
	{
		if (offset != 0)
		{
			strcpy(sentence + offset, " ");
			offset += 1;
		}
		size_t word_length = strlen(current->word);
		strcpy(sentence + offset, current->word);
		offset += word_length;
		current = current->next;
	} while (current != lst->head);

	sentence[total_length - 1] = '\0';
	return sentence;
}

void delete_node(list *lst, int index)
{
	node *target_node = find_node_at(lst, index);
	node *prev_node = target_node->prev;
	node *next_node = target_node->next;

	if (index == 0)
	{
		lst->head = next_node;
	}
	prev_node->next = next_node;
	next_node->prev = prev_node;

	free(target_node->word);
	free(target_node);
}

void delete_list(list *lst)
{
	while (lst->head != NULL)
	{
		delete_node(lst, 0);
	}
	free(lst);
	return;
}
