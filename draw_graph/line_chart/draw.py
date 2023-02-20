import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

myfont = FontProperties(size=30)

 
data1  = [0, 1, 2, 3, 4]
data2 = [0, 2, 4, 6, 8]

x = [0, 10, 100, 1000, 10000]
xTicsNum = range(len(x))

plt.figure(figsize=(15,8),dpi=100,linewidth = 2)
plt.plot(xTicsNum, data1, 'o-', color = 'g', label="d1")
plt.plot(xTicsNum, data2, 'o-', color = 'b', label="d2")
plt.title("title", fontproperties=myfont, x=0.5, y=1.03)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.xlabel("xlabel", fontsize=20, labelpad = 10)
plt.ylabel("ylabel", fontsize=20, labelpad = 20)

plt.legend(loc = "best", fontsize=10)
plt.xticks(xTicsNum, x)

for i, t in enumerate(data1):
    label = "({:}, {:})".format(i, t)
    plt.annotate(label, (i,t), textcoords="offset points",xytext=(-10,10),ha='center')

plt.show()
