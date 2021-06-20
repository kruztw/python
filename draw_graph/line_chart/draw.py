import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

myfont = FontProperties(size=40)

 
pcap_dump_rate  = [161, 181, 182, 180]
memcpy_rate = [105, 250, 480, 650]

cpu_num = [1, 2, 3, 4]

plt.figure(figsize=(15,10),dpi=100,linewidth = 2)
plt.plot(cpu_num, pcap_dump_rate,'o-',color = 'g', label="pcap_dump")
plt.plot(cpu_num, memcpy_rate,'o-',color = 'b', label="memcpy")

plt.title("Performance", fontproperties=myfont, x=0.5, y=1.03)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.xlabel("cpu # ", fontsize=30, labelpad = 15)
plt.ylabel("KPPS", fontsize=30, labelpad = 20)

plt.legend(loc = "best", fontsize=20)
plt.xticks([1, 2, 3, 4])

plt.show()
