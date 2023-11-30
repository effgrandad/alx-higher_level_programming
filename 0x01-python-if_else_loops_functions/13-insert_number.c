#include "lists.h"

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
        listint_t *node = *head, *new;

        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        new->m = val;

        if (node == NULL || node->m >= val)
        {
                new->next = node;
                *head = new;
                return (new);
        }

        while (node && node->next && node->next->m < val)
                node = node->next;

        new->next = node->next;
        node->next = new;

        return (new);
}
