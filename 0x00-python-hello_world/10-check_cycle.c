#include "lists.h"

/**
 * check_cycle - check a singly linked list has a cycle in it
 * @list: linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *new = list, *check = list;

	while (new && check  && check->next)
	{
		new = new->next;
		check  = check->next->next;
		if (new == check)
		{
			return (1);
		}
	}
	return (0);
}
