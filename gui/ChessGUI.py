import pygame

from sys import exit

SIZE = W, H = (600, 600)
WHITE = (255, 255, 255)



class ChessGUI:
    def __init__(self, chess_board):
        pygame.init()
        pygame.display.set_caption("Chess Monitor")

        self.screen = pygame.display.set_mode(SIZE)
        self.chess_board = chess_board

    def draw_chess_board(self):
        board_width, board_height = self.chess_board.size

        cell_width = W / board_width
        cell_height = H / board_height

        for i in range(board_width):
            for j in range(board_height):
                pygame.draw.rect(self.screen, (0, 0, 0),
                                 (i*cell_width, j*cell_height, cell_width, cell_height), 1)

        for pos in self.chess_board.figures_positions().values():
            pygame.draw.rect(self.screen, (0, 0, 0),
                             (int(pos[0]) * cell_width, int(pos[1]) * cell_height, cell_width, cell_height))


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.fill(WHITE)

            self.draw_chess_board()

            pygame.display.update()









