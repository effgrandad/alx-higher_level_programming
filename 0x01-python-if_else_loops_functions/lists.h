#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @m: integer
 * @next: pointer pointing to next node
 *
 * Description: a node struct of singly linked list
 *
 */
typedef struct listint_s
{
        int m;
        struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int m);
void free_listint(listint_t *head);
listint_t *insert_node(listint_t **head, int val);

#endif /* LISTS_H */

