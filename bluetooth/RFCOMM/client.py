import bluetooth

bd_addr = "1E:03:C6:9D:50:FD" # server 端的 addr

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()
