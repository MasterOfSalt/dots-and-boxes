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
        self.board[self.position_on_board(x,y)] = True
        self.available_moves.remove((x,y))
        return self.calc_score_for_set_line(x,y,player)

    def score(self,x,y,player):
        """method description
        :param _name_: _explanation
        """
        self.boxes[player-1] += 1
        self.board[self.position_on_board(x,y-1)] = player

    def position_on_board(self,x,y):
        """method description
        :param _name_: _explanation
        """
        return (x * self.dimensions[1] + y)
    def calc_score_for_set_line(self,x,y,player):
        """When a line is set this function detects if the player scored any points and adds them to the scoreboard
        :param _name_: _explanation
        """
        playagain = False
        pos = self.position_on_board(x,y)
        pos_1_to_left = self.position_on_board((x-1),y)
        pos_1_to_right = self.position_on_board((x+1),y)
        pos_2_to_left = self.position_on_board((x-2),y)
        pos_2_to_right = self.position_on_board((x+2),y)
        if x % 2 == 1:
            if y - 2 >= 0 and self.board[pos] and self.board[pos - 2] and self.board[pos_1_to_left - 1] and self.board[pos_1_to_right - 1]:
                playagain = True
                self.score(x,y,player)
            if (y + 2 < self.dimensions[1]) and self.board[pos] and self.board[pos + 2] and self.board[pos_1_to_left + 1]  and self.board[pos_1_to_right + 1]:
                playagain = True
                self.score(x,y,player)
        else:
            if x - 2 >= 0 and self.board[pos] and self.board[pos_2_to_left] and self.board[pos_1_to_left - 1] and self.board[pos_1_to_left + 1]:
                playagain = True
                self.score(x,y,player)
            if (x + 2 < self.dimensions[0]) and self.board[pos] and self.board[pos_2_to_right] and self.board[pos_1_to_right - 1] and self.board[pos_1_to_right+ 1]:
                playagain = True
                self.score(x,y,player)
        return playagain


    def copy(self):
        """method description
        :param _name_: _explanation
        """
        csb = Coins_strings_board()
        csb.dimensions = self.dimensions
        #shallow copies
        csb.board = self.board[:]
        csb.available_moves = self.available_moves[:]
        csb.boxes = self.boxes[:]
        return csb
