#include <Python.h>

/**
 * print_python_list - Prints Python list info
 * @p: PyObject list
 */
void print_python_list(PyObject *p)
{
Py_ssize_t i, size;

printf("[*] Python list info\n");
size = PyList_Size(p);
printf("[*] Size of the Python List = %lu\n", size);
printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
printf("Element %lu: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
if (strcmp(Py_TYPE(PyList_GetItem(p, i))->tp_name, "bytes") == 0)
print_python_bytes(PyList_GetItem(p, i));
}
}

/**
 * print_python_bytes - Prints Python bytes object info
 * @p: PyObject bytes
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *str;

printf("[.] bytes object info\n");
size = PyBytes_Size(p);
printf("  size: %lu\n", size);
str = PyBytes_AsString(p);
printf("  trying string: %s\n", str);

if (size > 10)
size = 10;
else
size++;

printf("  first %lu bytes: ", size);
for (i = 0; i < size; i++)
printf("%02hhx%c", str[i], i + 1 < size ? ' ' : '\n');
}
