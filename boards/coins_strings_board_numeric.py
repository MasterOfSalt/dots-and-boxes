import numpy as np

PLAYER1 = -1
PLAYER2 = 1
PLAYERS = {'B': -1, 'W': 1}

class Coins_strings_board(object):
    def __init__(self, rows, cols):
        self.rows, self.cols = rows, cols
        self.score = [0, 0] # B, W
        self.board = np.zeros((2*(rows+1)-1, 2*(cols+1)-1), dtype=np.int)
        self.r, self.c = self.board.shape
        self._edges = np.reshape([i%2 != j%2 for j in range(self.c) for i in range(self.r)], (self.r, self.c))
        self.num_boxes = (rows-1) * (cols-1)

    def free_lines(self):
        unplayed = np.logical_not(self.board)
        moves = np.where(np.logical_and(unplayed, self._edges))
        list1 = list(zip(moves[0].astype(int), moves[1].astype(int)))
        return list1

    def fill_line(self,player,i,j):
        self.board[i,j] = player
        vertical = i%2 > j%2
        if vertical:
            self._check_box(player, i, j-1)
            self._check_box(player, i, j+1)
        else:
             self._check_box(player, i-1, j)
             self._check_box(player, i+1, j)



    def _check_box(self, player, i, j):
        if (i and i < self.r) and (j and j < self.c):
            filled = self.board[i-1, j] and self.board[i+1, j] and self.board[i, j-1] and self.board[i, j+1]
            if filled:
                self.score[player == 1] += 1
            return filled
