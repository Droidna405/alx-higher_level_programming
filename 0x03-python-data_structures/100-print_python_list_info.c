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

if (!PyList_Check(p))
{
printf("[-] TypeError: cannot use anything other than\
 list with this function\n");
return;
}

Py_ssize_t size = PyList_Size(p);
  
printf("[*] Size of the Python List = %zd\n", size);

PyObject *first_element = PyList_GetItem(p, 0);


if (first_element == NULL)
{
PyErr_Print();
return;
}

PyObject *first_element_type = PyList_GetItem(p, 0);
if (first_element_type == NULL)
{
PyErr_Print();
return;
}

printf("[*] First element type: ");

printf("%s\n", PyType_Type.tp_name(first_element_type));

Py_DECREF(first_element);
Py_DECREF(first_element_type);
}
