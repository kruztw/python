#include <Python.h>

int add(int a, int b) {
    return a + b;
}

static PyObject *_add(PyObject *self, PyObject *args, PyObject *kwargs) {
    int a, b = 2; // default value of b is 2
    static char *kwlist[] = {"a", "b", NULL};
    int res;

    // parse arguments
    // i|i : non-optional args | optional args
    // i: int
    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "i|i", kwlist, &a, &b))
        return NULL;

    res = add(a, b);

    // Wrap the return value into PyObject
    return Py_BuildValue("i", res);
}


// Construct the Module's Method Table (list the methods to expose)
static PyMethodDef myMethods[] = {
    // slow_calc method takes in both positional & keyword parameters
    {"add", (PyCFunction) _add, METH_VARARGS | METH_KEYWORDS, "add func"},
    // Ends with an entry with NULL values
    {NULL, NULL, 0, NULL}
};


// Define the module structure
static struct PyModuleDef myModule = {
    PyModuleDef_HEAD_INIT,
    "foo",
    "my add is an add function",
    -1, // global state
    myMethods
};

// Init method to be called when module gets imported in Python
PyMODINIT_FUNC PyInit_foo() {
    return PyModule_Create(&myModule);
}
