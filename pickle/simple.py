# https://zhuanlan.zhihu.com/p/89132768

import pickle
import pickletools
import os

class Student():
    def __init__(self):
        self.name = "kruztw"
        self.grade = "G2"
    def __reduce__(self):
        return (os.system, ('ls', )) # 反序列化會自動值行, 萬惡之源


x = Student()
s1 = pickle.dumps(x,protocol=3) # protocol: 指定版本 (option)
s2 = pickletools.optimize(s1)
print(s1)
pickletools.dis(s1)


print("---------------------------")
print(s2)
pickletools.dis(s2)

pickle.loads(s2)



"""
opcode: https://github.com/python/cpython/blob/3.9/Lib/pickle.py

opcode: 1bytes

\x80: 字串開頭
\x80\x03: 版本 3

c : 稱為 GLOBAL 操作符, 透過 find_class 讀取連續兩個字串 (module, nmae), 以 \n 分割

) : push
\x81 : pop => args, pop => cls, 執行 cls.__new__(cls, *args)
} : push an empty dictionary to stack
( : MARK (load_mark) , 將當前 stack 放到前序 stack, 並清空當前 stack                  (進入 function)
V : 讀入字串到 stack, 以 \n 結尾
u : pop_mark, 把當前 stack 內容存成 array, 然後把當前 stack 恢復到 MARK 時的狀態      (離開 function)
    並將 array 內容讀到 dictionary (stack 頂部)
b : BUILD, pop => 存進 state, pop => inst, 若 inst 有 __setstate__ 則用 __setstate__ 處理
    否則存成 inst.__dict__ 到 stack
. : STOP, 回傳 stack top
R : REDUCE, pop => args, pop => f, push f(args)

若 STOP 後 stack 有超過一個元素, dis 會噴錯, loads 不會
"""
