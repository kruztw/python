/* Define module name */
%module FOO

/* Insert code into generated C wrapper code */
%{
#include "simple.h"
%}

/* List declarations */
int add(int a = 0, int b = 0);
