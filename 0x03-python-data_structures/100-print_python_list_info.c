#include <Python.h>

/**
 * print_python_list_info - Prints basic information about a Python list
 * @p: Pointer to PyObject (assumed to be a list)
 */
void print_python_list_info(PyObject *p)
{
Py_ssize_t size, i;
PyObject *item;

size = PyList_Size(p);
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
}
}
