#!/usr/bin/env python3
# 參考: https://fredrikj.net/python-flint/

from flint import nmod_mat, fmpz_mat

'''
A = | 1 1 1 |
    | 1 2 1 |
    | 1 1 2 |

B = | 6 |
    | 8 |
    | 9 |

A * X = B
X = ?
'''

A = [[1,1,1],[1,2,1],[1,1,2]]
B = [6, 8, 9]
MA = fmpz_mat(A)
MB = fmpz_mat(3,1, B)
MX = MA.solve(MB).entries()
print(MX)


A = [[1,1,1],[1,2,1],[1,1,2]]
B = [6, 8, 9]
MA = nmod_mat(A, 10000)
MB = nmod_mat(3,1, B, 10000)
MX = MA.solve(MB).entries()
print(MX)
