#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * struct listint_s - a singly limked list
 * @n: integer
 * @next: pointer pointing to the next node
 *
 * Description: a node structure of singly linked list
 * for Holberton project
 */
typedef struct listint_s
{
  int n;
  struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **headd, const int n);
void free_listint(listint_t *headd);

int aux_palind(listint_t **headd);
int is_palindrome(listint_t **headd);

#endif /* LISTS_H vi
