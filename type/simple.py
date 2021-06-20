a = 1
print(type(a))
print(type(a)(123))
print(type(a)('123'))
print(type(type(a)('123')))
# print(type(a)('abc'))  # error

print('--------------------------')

a = "1"
print(type(a))
print(type(a)('abc'))
print(type(a)(123))
print(type(type(a)(123)))

print('--------------------------')

a = []
print(type(a))
print(type(a)([1, 'a']))
