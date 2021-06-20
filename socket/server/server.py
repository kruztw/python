# nc localhost 8888

import socketserver

class Task(socketserver.BaseRequestHandler):

    def recv(self):
        return self.request.recv(1024).strip()

    def send(self, msg):
        self.request.sendall(msg + b'\n')

    def handle(self):
        self.request.sendall(b'input: ')
        user_input = self.recv()
        self.send(b'recv: '+user_input)

class ForkingServer(socketserver.ForkingTCPServer, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 8888
    print(HOST, PORT)
    server = ForkingServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
