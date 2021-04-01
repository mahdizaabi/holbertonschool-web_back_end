#include <stdio.h>
#include <stdlib.h>

#include "search.h"

skiplist_t *linear_skip(skiplist_t *list, int value)
{

    if (list == NULL)
    {
        return NULL;
    }
    skiplist_t *scooter = NULL;
    scooter = list;
    while (scooter->express != NULL)
    {
        if (scooter->express->n == value)
        {
            return (scooter->index);
        }
        if (scooter->express->n > value)
        {
            while (scooter->next != NULL)
            {
                if (scooter->n == value)
                {
                    return (scooter->index);
                }
                scooter = scooter->next;
            }
        }
        scooter = scooter->express;
    }
    return NULL;
}