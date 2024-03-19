#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to a pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
if (*head == NULL || (*head)->next == NULL)
return (1); /* Empty list or single node list is a palindrome */

listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev_slow = *head;
listint_t *second_half = NULL;
listint_t *mid_node = NULL;
int is_palindrome = 1; /* Assume it's a palindrome by default */

/* Find the middle of the list using slow and fast pointers */
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev_slow = slow;
slow = slow->next;
}

/* Handle odd number of nodes by skipping the middle node */
if (fast != NULL)
{
mid_node = slow;
slow = slow->next;
}

/* Reverse the second half of the list */
second_half = reverse_list(slow);
prev_slow->next = NULL; /* Terminate the first half */

/* Compare the first half with the reversed second half */
listint_t *p1 = *head;
listint_t *p2 = second_half;
while (p1 != NULL && p2 != NULL)
{
if (p1->n != p2->n)
{
is_palindrome = 0;
break;
}
p1 = p1->next;
p2 = p2->next;
}

/* Restore the original list by reversing the second half again */
second_half = reverse_list(second_half);

/* Reconnect the first and second halves if they were originally connected */
if (mid_node != NULL)
{
prev_slow->next = mid_node;
mid_node->next = second_half;
}
else
{
prev_slow->next = second_half;
}

return (is_palindrome);
}

/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to the head of the linked list.
 *
 * Return: Pointer to the head of the reversed linked list.
 */
listint_t *reverse_list(listint_t *head)
{
listint_t *prev = NULL;
listint_t *current = head;
listint_t *next = NULL;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

return (prev);
}
