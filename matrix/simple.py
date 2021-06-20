#!/usr/bin/env python3
# 參考: https://fredrikj.net/python-flint/

from flint import nmod_mat, fmpz_mat

'''
A = | 1 1 1 |
    | 1 2 1 |
    | 1 1 2 |
'''

A = [[1,1,1],[1,2,1],[1,1,2]]
MA = fmpz_mat(A)
print(MA,"\n")


MA = MA.transpose()
print(MA,"\n")


MA = MA.entries()
print(type(MA))
