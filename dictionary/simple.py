def myprint(msg, arg):
    print(msg.ljust(10, ' '), arg)


dic = {}
dic2 = {'c': 3}


dic['a'] = 1
dic['b'] = 2
myprint("add:", dic)

dic.update(dic2)
myprint("update:", dic)


dic.pop('c')
myprint("pop:", dic)


dic_copy = dic.copy()
dic_copy['a'] = 10
myprint("copy:", dic)

dic_copy = dic
dic_copy['a'] = 10
myprint("assign:", dic)


dic.clear()
myprint("clear:", dic)


del dic
# print(dic) # error not defined

