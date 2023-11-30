#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * insert_node - adds a value to a singly-linked list is sorted
 * @head: pointer pointing to the head of the linked list
 * @val: The value to add
 *
 * Return:  - NULL upon failure.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int val)
{
	listint_t *current = *head;
	listint_t *tmp = NULL;
	listint_t *new = NULL;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = val;
	new->next = NULL;

	if (!*head || (*head)->n > val)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (current && current->n < val)
		{
			tmp = current;
			current = current->next;
		}

		tmp->next = new;
		new->next = current;
	}
	return (new);
}
