



class Board:
    def __init__(self):
        self.size = (8, 8)
        self._figures_positions = dict()
        self.score = 0

    def set_size(self, size):
        self.size = size

    def set_positions(self, positions):
        self._figures_positions.update(positions)

    def figures_positions(self):
        return self._figures_positions

    def set_score(self, score):
        self.score = score


