#include <stdio.h>
#include <stdlib.h>
#include "search.h"

/**
 * linear_skip - Entry point
 * @list: head of skiplist
 * @value: value to search
 * Return: Always EXIT_SUCCESS
 */
skiplist_t *linear_skip(skiplist_t *list, int value)
{

	if (list == NULL)
		return (NULL);
	skiplist_t *scooter = list;
	skiplist_t *tempScooter = NULL;
	size_t tempIndex = 0;
	char *check = "Value checked at index [%lu] = [%d]\n";
	char *found = "Value found between indexes [%lu] and [%lu]\n";

	while (scooter->express != NULL)
	{
		if (scooter->express->n == value)
		{
			printf("Value checked at index [%lu] = [%d]\n", scooter->index, scooter->n);
			return (scooter);
		}
	if (scooter->express->n > value)
	{
		printf(check, scooter->express->index, scooter->express->n);
		printf(found, scooter->index, scooter->express->index);
		while (scooter->next != NULL)
		{
			printf("Value checked at index [%lu] = [%d]\n", scooter->index, scooter->n);
			if (scooter->n == value)
				return (scooter);
			scooter = scooter->next;
		}
	}
	scooter = scooter->express;
	printf("Value checked at index [%lu] = [%d]\n", scooter->index, scooter->n); }
	tempScooter = scooter;
	tempIndex = scooter->index;
	while (scooter->next != NULL)
		scooter = scooter->next;
	printf(found, tempIndex, scooter->index);
	while (tempScooter->next != NULL)
	{
		printf(check, tempScooter->index, tempScooter->n);
		tempScooter = tempScooter->next; }
	return (NULL);
}
