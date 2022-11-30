#include "lists.h"

/**
 * insert_node - insertedPoint
 * @head: head
 * @number: value
 * Return:  The address of the new node or NULL if failure
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *nNode, *fNode;

fNode = *head;

nNode = malloc(sizeof(listint_t));
if (nNode == NULL)
return (NULL);
nNode->n = number;

if (*head == NULL || (*head)->n > number)
{
nNode->next = *head;
*head = nNode;
return (nNode);
}

while (fNode->next != NULL)
{
if ((fNode->next)->n >= number)
{
nNode->next = fNode->next;
fNode->next = nNode;
return (nNode);
}
fNode = fNode->next;
}
fNode->next = nNode;
nNode->next = NULL;
return (nNode);
}
