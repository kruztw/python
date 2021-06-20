func = lambda x: print(x)
func(1)

(lambda x: print(x))(1)                 # python2 labmda 運算式不能放 print

print((lambda: 5)())

ans = ( lambda x: (lambda: x+x)() )(2)  # x 用 2 帶入, 丟入 (labmda: x+x)(), 回傳 4
print(ans)



f = lambda x: x
g = lambda x: x+1
ans = f(g)(1)                                 # f(g) = h , return h(1)
print(ans)

ans = (lambda x: x)(lambda x: x+1)(1)         # (lambda x: x)(lambda x: x+1) == lambda x: x+1
print(ans)
