#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head;
listint_t *prev_slow = NULL;
listint_t *second_half, *mid_node = NULL;
int is_palindrome = 1;

if (*head == NULL || (*head)->next == NULL)
return (1);

while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;

prev_slow = slow;
slow = slow->next;
}

if (fast != NULL)
{
mid_node = slow;
slow = slow->next;
}

second_half = slow;
prev_slow->next = NULL;

listint_t *prev = NULL, *current = second_half, *next;
while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
second_half = prev;

listint_t *first_half = *head;
while (second_half != NULL)
{
if (first_half->n != second_half->n)
{
is_palindrome = 0;
break;
}
first_half = first_half->next;
second_half = second_half->next;
}

prev = NULL;
current = mid_node;
while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
if (prev_slow != NULL)
prev_slow->next = prev;
else
*head = prev;

return (is_palindrome);
}
