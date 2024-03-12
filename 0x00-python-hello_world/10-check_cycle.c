#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
listint_t *slow_ptr = list;
listint_t *fast_ptr = list;

while (slow_ptr != NULL && fast_ptr != NULL && fast_ptr->next != NULL)
{
slow_ptr = slow_ptr->next;
fast_ptr = fast_ptr->next->next;

if (slow_ptr == fast_ptr)
return (1);
}

return (0);
}
