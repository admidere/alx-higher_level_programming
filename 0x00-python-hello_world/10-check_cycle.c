#include "lists.h"
#include <stdlib.h>
/**
 *check_cycle-checks the presence of cycle
 *@list: pointer to listint_t
 *Return: int
 */
int check_cycle(listint_t *list)
{
listint_t *j, *n;

if (!list || !list->next)
return (0);

n = list;
j = list->next;

while (j && j->next && n && n->next)
{
if (j == n)
return (1);
j = j->next->next;
if (!j)

break;
n = n->next;
}
return (0);
}
