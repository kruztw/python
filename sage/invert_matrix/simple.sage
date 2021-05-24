# sage simple.sage

#### 一般 invert
print(Matrix([[1, 2], [3,4]]).inverse())


#### 有 module 的 invert => A * A^-1 = I  (在 element mod 7 的情況)
print(Matrix(IntegerModRing(7), [[1, 2], [3,4]]).inverse())



