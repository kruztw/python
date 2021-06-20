from signal import signal, alarm, SIGALRM

def timeout(a, b):
    print("time's up")
    exit()

signal(SIGALRM, timeout)
alarm(1) 
input('>')
