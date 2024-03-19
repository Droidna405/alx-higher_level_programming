#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * find_middle - Finds the middle node of a linked list.
 * @head: Pointer to the head of the linked list.
 * @mid_node: Pointer to store the middle node.
 *
 * Return: Pointer to the second half of the linked list.
 */
listint_t *find_middle(listint_t *head, listint_t **mid_node)
{
listint_t *slow = head;
listint_t *fast = head;


while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
slow = slow->next;
}
if (fast != NULL)
{
*mid_node = slow;
slow = slow->next;
}

return (slow);
}

/**
 * compare_lists - Compares two linked lists.
 * @head1: Pointer to the head of the first linked list.
 * @head2: Pointer to the head of the second linked list.
 *
 * Return: 1 if the lists are identical, 0 otherwise.
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
while (head1 != NULL && head2 != NULL)
{
if (head1->n != head2->n)
return (0);
head1 = head1->next;
head2 = head2->next;
}
return (1);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to a pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
if (*head == NULL || (*head)->next == NULL)
return (1);

listint_t *mid_node = NULL;
listint_t *second_half = find_middle(*head, &mid_node);
listint_t *prev_slow = mid_node;
listint_t *first_half = *head;
int result = 1;

second_half = reverse_list(second_half);
result = compare_lists(first_half, second_half);

second_half = reverse_list(second_half);

if (mid_node != NULL)
{
prev_slow->next = mid_node;
mid_node->next = second_half;
}
else
{
prev_slow->next = second_half;
}

return (result);
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

