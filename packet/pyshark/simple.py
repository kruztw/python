# 參考 : https://www.gushiciku.cn/pl/pbUB/zh-tw

import pyshark

# 讀取 pcap 檔
cap = pyshark.FileCapture('./test.pcap')
for packet in cap:
    if 'ICMP' in packet:
        print(packet['IP'].dst, packet['ICMP'].data)

# 抓封包
#capture = pyshark.LiveCapture(interface='wlo1')
#capture = pyshark.LiveRingCapture(interface='eth0')
#capture = pyshark.RemoteCapture('192.168.1.101', 'eth0')
#capture.sniff(timeout=5)
#print(capture)
#print(capture[0])

# 抓封包並解密
#cap1 = pyshark.FileCapture('test.pcap', decryption_key='password')
#cap2 = pyshark.LiveCapture(interface='wlo1', decryption_key='password',encryption_type='wpa-psk')

# 顯示支援的加密形式
#print(pyshark.FileCapture.SUPPORTED_ENCRYPTION_STANDARDS)
#print(pyshark.LiveCapture.SUPPORTED_ENCRYPTION_STANDARDS)



