#!/usr/bin/env python3
# encoding: utf-8
"""
coins_strings_board.py

__ for the Machine Learning Project course at KU Leuven (2017-2018)

"""
class Coins_strings_board:
    def __init__(self,nb_rows=0,nb_cols=0):
        """Create board that uses coins and strings for its represenation.
        :param nb_rows: Rows in grid
        :param nb_cols: Columns in grid
        """
        #rows en cols in #dots
        self.board = [None] * ((2 * nb_rows -1) * (2 * nb_cols-1))
        #expressed in number of symbols and not rows/cols in grid
        self.dimensions = (nb_rows * 2 - 1, nb_cols * 2 - 1)
        self.available_moves = self.free_lines()
        self.boxes = [0, 0] # Player 2, Player 1

    def free_lines(self):
        """method description
        :param _name_: _explanation
        """
        moves, i = [], 1
        for cel in self.board[1::2]:
            if not cel:
                moves.append((i // self.dimensions[1], i % self.dimensions[1]))
            i += 2
        return moves

    def fill_line(self,x,y,player):
        """method description
        :param _name_: _explanation
        """
        self.board[x * self.dimensions[1] + y] = True
        self.available_moves.remove((x,y))
        return self._close_box(x,y,player)


    def _close_box(self,x,y,player):
        """method description
        :param _name_: _explanation
        """
        completed = False
        if x % 2 == 1: # horizontal
            if y - 2 >= 0 and self.board[x * self.dimensions[1] + y] and self.board[x * self.dimensions[1] + y - 2] and self.board[(x - 1) * self.dimensions[1] + y - 1] and self.board[(x + 1) * self.dimensions[1] + y - 1]:
                completed = True
                self.boxes[player-1] += 1
                self.board[x * self.dimensions[1] + y - 1] = player
            if (y + 2 < self.dimensions[1]) and self.board[x * self.dimensions[1] + y] and self.board[x * self.dimensions[1] + y + 2] and self.board[(x - 1) * self.dimensions[1] + y + 1]  and self.board[(x + 1) * self.dimensions[1] + y + 1]:
                completed = True
                self.boxes[player-1] += 1
                self.board[x * self.dimensions[1] + y + 1] = player
        else:
            if x - 2 >= 0 and self.board[x * self.dimensions[1] + y] and self.board[(x - 2) * self.dimensions[1] + y] and self.board[(x - 1) * self.dimensions[1] + y - 1] and self.board[(x - 1) * self.dimensions[1] + y + 1]:
                completed = True
                self.boxes[player-1] += 1
                self.board[(x - 1) * self.dimensions[1] + y] = player
            if (x + 2 < self.dimensions[0]) and self.board[x * self.dimensions[1] + y] and self.board[(x + 2) * self.dimensions[1] + y] and self.board[(x + 1) * self.dimensions[1] + y - 1] and self.board[(x + 1) * self.dimensions[1] + y + 1]:
                completed = True
                self.boxes[player-1] += 1
                self.board[(x + 1) * self.dimensions[1] + y] = player
        return completed



    def copy(self):
        """method description
        :param _name_: _explanation
        """
        dab = Coins_strings_board()
        dab.dimensions = self.dimensions
        #shallow copies
        dab.board = self.board[:]
        dab.available_moves = self.available_moves[:]
        dab.boxes = self.boxes[:]
        return dab
