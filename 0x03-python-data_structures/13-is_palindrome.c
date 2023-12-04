#include "lists.h"

/**
 * palidrom - recursive palind or error
 * @headd: head list
 * Return: if not palindrome 0
 * if palidrome 1
 */
int is_palindrome(listint_t **headd)
{
	if (headd == NULL || *headd == NULL)
		return (1);
	return (aux_palin(headd, *headd));
}
/**
 * aux_palid - funct to determine if is palindrome
 * @headd: head list
 * end: end list
 */
int aux_palind(listint_t **headd, listint_t end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(headd, end->next) && (*headd)-> == end->n)
	{
		*headd = (*headd)->next;
		return (1);
	}
	return (0);
}
