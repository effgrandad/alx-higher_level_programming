#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @headd: pointer to the first node in the list
 *
 * Return: pointer pointing to the first node in the new list
 */
void reverse_listint(listint_t **headd)
{
  listint_t *prev = NULL;
  listint_t *current = *headd;
  listint_t *next = NULL;

  while (current)
    {
      next = current->next;
      current->next = prev;
      prev = current;
      current = next;
    }

  *headd = prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @headd: double pointer pointing to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **headd)
{
  listint_t *slow = *headd, *fast = *headd, *tmp = *headd, *dup = NULL;

  if (*headd == NULL || (*headd)->next == NULL)
    return (1);

  while (1)
    {
      fast = fast->next->next;
      if (!fast)
	{
	  dup = slow->next;
	  break;
	}
      if (!fast->next)
	{
	  dup = slow->next->next;
	  break;
	}
      slow = slow->next;
    }

  reverse_listint(&dup);

  while (dup && tmp)
    {
      if (tmp->n == dup->n)
	{
	  dup = dup->next;
	  tmp = tmp->next;
	}
      else
	return (0);
    }

  if (!dup)
    return (1);

  return (0);
}

