src1 = '''
print("multi statements")
a = 1
'''

c = compile(src1, '', 'exec')
exec(c)


src2 = 'print("single interactive statement")'
c = compile(src2, '', 'single')
exec(c)

src3 = 'a + 5'
c = compile(src3, '', 'eval')
ans = eval(c)
print(ans)
