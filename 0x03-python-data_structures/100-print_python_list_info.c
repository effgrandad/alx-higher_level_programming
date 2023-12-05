#include <Python.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * print_python_list_info - Displays info about basic Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, x;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (x = 0; x < size; x++)
	{
		printf("Element %d: ", x);

		obj = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}

