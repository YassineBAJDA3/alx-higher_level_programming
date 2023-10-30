#include<stdio.h>
#include<stdlb.h>
#include "lists.h"

/**
 * Check_cycle - checks if list is cyclical
 * @list: pointer to list to cheeck
 * Return: 1 if cyclical, 0 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;
	while (fast && fast->next)
		{
			slow = slow->next;
			fast = fast->next->next;
			if (slow == fast)
				return (1);
		}
	return (0);
}
