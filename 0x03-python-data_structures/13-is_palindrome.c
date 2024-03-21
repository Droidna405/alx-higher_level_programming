#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a double pointer to the head of the linked list
 *
 * Return: If the list is a palindrome - 1.
 *         Otherwise - 0.
 */
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head;
listint_t *prev_slow = NULL, *second_half = NULL;

/* Get the middle of the list using two pointers */
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev_slow = slow;
slow = slow->next;
}

/* If fast is not NULL, the list has odd length, so skip the middle node */
if (fast != NULL)
slow = slow->next;

/* Reverse the second half of the list */
second_half = slow;
prev_slow->next = NULL;  // Mark the end of first half

while (second_half != NULL)
{
listint_t *next = second_half->next;
second_half->next = *head;
*head = second_half;
second_half = next;
}

/* Compare first and second half for palindrome */
slow = *head;
fast = second_half;
int is_palin = 1;
while (slow != NULL && fast != NULL)
{
if (slow->n != fast->n)
{
is_palin = 0;
break;
}
slow = slow->next;
fast = fast->next;
}

/* Restore the original list */
second_half = *head;
*head = slow;
while (second_half != NULL)
{
listint_t *next = second_half->next;
second_half->next = *head;
*head = second_half;
second_half = next;
}

return (is_palin);
}
