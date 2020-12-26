import pygame

from sys import exit

SIZE = W, H = (600, 600)
WHITE = (255, 255, 255)
LIGHT_ORANGE = (255, 162, 106)
BLACK = (0, 0, 0)
BEIGE = (245, 245, 220)
DARK_BROWN = (101, 67, 33)
RED = (255, 0 , 0)


class ChessGUI:
    def __init__(self, chess_board, client):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Chess Monitor")

        self.myfont = pygame.font.SysFont('serif', 15)

        self.client = client

        self.screen = pygame.display.set_mode(SIZE)
        self.chess_board = chess_board

        self.queen_img = pygame.image.load('../gui/img/queen2.png').convert_alpha()
        self.rook_img = pygame.image.load('../gui/img/rook2.png').convert_alpha()
        self.bishop_img = pygame.image.load('../gui/img/bishop2.png').convert_alpha()

        self.queen_img.set_colorkey((255, 255, 255))
        self.rook_img.set_colorkey((255, 255, 255))
        self.bishop_img.set_colorkey((255, 255, 255))

        self.imgs = {'q': self.queen_img, 'b' : self.bishop_img, 'r': self.rook_img}



    def draw_chess_board(self):
        board_width, board_height = self.chess_board.size

        cell_width = int(self.screen.get_width() / board_width)
        cell_height = int(self.screen.get_height() / board_height)

        for i in range(board_width):
            for j in range(board_height):
                col = BEIGE if (i + j) % 2 == 0 else DARK_BROWN

                pygame.draw.rect(self.screen, col,
                                 (i * cell_width, j * cell_height, cell_width, cell_height))

                pygame.draw.rect(self.screen, BLACK,
                                 (i*cell_width, j*cell_height, cell_width, cell_height), 1)


        chess_dict = self.chess_board.figures_positions()
        for fig_name in chess_dict.keys():
            pos = chess_dict[fig_name]
            if fig_name[0] == 'q' or fig_name[0] == 'r' or fig_name[0] == 'b':
                scale = pygame.transform.scale(self.imgs[fig_name[0]], (cell_width, cell_height))
                scale_rect = scale.get_rect(topleft=(pos[0] * cell_width, pos[1] * cell_height))
                self.screen.blit(scale, scale_rect)
            else:
                pygame.draw.rect(self.screen, (0, 0, 0),
                                 (pos[0] * cell_width, pos[1] * cell_height, cell_width, cell_height))

        if self.chess_board.score != 0:
            textsurface = self.myfont.render(f'# of Itterations: {self.chess_board.score}', True, BLACK)
            self.screen.blit(textsurface, (15, 15))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.client.start()

            self.screen.fill(WHITE)

            self.draw_chess_board()

            pygame.display.update()




