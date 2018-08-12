#!/usr/bin/env python3
# encoding: utf-8
"""
strings_board.py

__ for the Machine Learning Project course at KU Leuven (2017-2018)

"""
"""
from:"Chapter 16: Dots-and-Boxes", Winning Ways for your Mathematical Plays, Volume 2: Games in Particular, Academic Press, pp. 507–550.
Dots and Boxes has a dual graph form called "Strings-and-Coins".
 This game is played on a network of coins (vertices) joined by strings (edges).
 Players take turns cutting a string.
 When a cut leaves a coin with no strings, the player "pockets" the coin and takes another turn.
 The winner is the player who pockets the most coins.
 Strings-and-Coins can be played on an arbitrary graph
"""
class Strings_board:
    def __init__(self,nb_rows=0,nb_cols=0):
        """Create board that only uses strings for its represenation.
        :param nb_rows: Rows in grid
        :param nb_cols: Columns in grid
        """
        even = [False for i in range(nb_cols)]
        odd = [False for i in range(nb_cols+1)]
        self.board = []
        self.nb_rows = nb_rows
        self.nb_cols = nb_cols
        for i in range(nb_rows * 2 + 1):
            if i % 2 == 0:
                self.board.append(even[:])
            else:
                self.board.append(odd[:])
    def fill_line(self,x,y):
        """method description
        :param x: _explanation
        """
        self.board[x][y] = True

    def get_potential_moves(self):
        """method description
        :param _name_: _explanation
        """
        potential_moves = []
        for i, row in enumerate(self.board):
            for j, val in enumerate(row):
                if val == False:
                    potential_moves.append((i,j))
        return(potential_moves)

    def number_of_borders(self,box):
        """method description
        :param _name_: _explanation
        """
        return [self.board[int(box[0]) * 2][int(box[1])],self.board[int(box[0]) * 2 + 1][int(box[1])],self.board[int(box[0]) * 2 + 1][int(box[1]) + 1],self.board[int(box[0]) * 2 + 2][int(box[1])]]


    def find_boxes(self,line):
        """method description
        :param _name_: _explanation
        """
        num = 0
        if line[0] % 2 == 0:
            if line[0] > 0:
                number_of_borders = self.number_of_borders(((line[0]-1)/2, line[1]))
                if sum(number_of_borders)>= 2:
                    num += 1
            if (line[0]-1)/2+1 < self.nb_cols -1:
                number_of_borders = self.number_of_borders(((line[0]-1)/2+1, line[1]))
                if sum(number_of_borders)>= 2:
                    num += 1
        else:
            if line[1] > 0:
                number_of_borders = self.number_of_borders(((line[0]-1)/2, line[1]-1))
                if sum(number_of_borders)>= 2:
                    num += 1
            if line[1] < self.nb_cols:
                number_of_borders = self.number_of_borders(((line[0]-1)/2, line[1]))
                if sum(number_of_borders)>= 2:
                    num += 1
        return num
