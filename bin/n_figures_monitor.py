
from chess.board import Board
from client.ChessMonitorClient import ChessMonitorClient
from gui.ChessGUI import ChessGUI





if __name__ == '__main__':
    b = Board()

    client = ChessMonitorClient(b)
    client.init()

    gui = ChessGUI(b, client)
    gui.run()








