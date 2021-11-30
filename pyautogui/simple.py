# 參考: https://yanwei-liu.medium.com/pyautogui-%E4%BD%BF%E7%94%A8python%E6%93%8D%E6%8E%A7%E9%9B%BB%E8%85%A6-662cc3b18b80


import pyautogui as p

print("screen size: ", p.size())

print(p.position())
p.moveTo(x=100, y = 100, duration=1) # 1s
print(p.position())
p.click(x = 200, y = 200)
print(p.position())
p.doubleClick(300, 300)
print(p.position())

p.typewrite('Hello world!', interval=0.25)
