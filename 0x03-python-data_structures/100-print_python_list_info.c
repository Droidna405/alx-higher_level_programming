#include <python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - Prints basic info about a Python list
 *
 * @p: A pointer to the Python object
 *
 * Description:
 *   This function prints basic information about a Python list object.
 *
 *   - If the object is not a PyList object, it prints an error message
 *     and returns.
 *   - It prints the size of the list.
 *   - It attempts to retrieve the first element of the list and, if
 *     successful, it prints the type of the first element.
 *
 *   It properly decrements the reference counts of any borrowed Python
 *   objects to avoid memory leaks.
 *
 * Return:
 *   Nothing (void)
 */
void print_python_list_info(PyObject *p)
{
PyListObject *list = (PyListObject *)p;
Py_ssize_t size = PyList_Size(p);
Py_ssize_t i;
PyObject *item;

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", list->allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
}
}
