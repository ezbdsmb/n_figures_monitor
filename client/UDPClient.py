import socket


class UDPClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def sendto(self, message, server_addr):
        self.sock.sendto(bytes(message, "utf-8"), server_addr)

    def recvfrom(self):
        data, addr = self.sock.recvfrom(1024)
        return str(data, "utf-8"), addr