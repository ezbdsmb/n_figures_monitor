import threading

from client.UDPClient import UDPClient
from client.msg_parser import parse_cmd


class ChessMonitorClient(UDPClient):
    def __init__(self, chess_board, server_addr=("localhost", 9998)):
        super().__init__()
        self.client_thread = threading.Thread(target=self.__recv_loop)
        self.client_thread.daemon = True
        self.server_addr = server_addr
        self.chess_board = chess_board

    def init(self):
        self.sendto('init_monitor', self.server_addr)
        data, addr = self.recvfrom()

        print('Received', data, 'from', addr)

        self.client_thread.start()

    def start(self):
        reqs = ['set_params 12 12', 'start_solving']

        for req in reqs:
            self.sendto(req, self.server_addr)

    def __recv_loop(self):
        while True:
            data, addr = self.recvfrom()
            print('Received', data, 'from', addr)

            type, param = parse_cmd(data)

            if type == 'board_size':
                print(type, param)
                self.chess_board.set_size(param)
            elif type == 'board':
                print(type, param)
                self.chess_board.set_positions(param)





