#!/usr/bin/env python3
# encoding: utf-8
"""
strings_board.py

__ for the Machine Learning Project course at KU Leuven (2017-2018)

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
    def closest_free(self,x, y):
        """method description
        :param _name_: _explanation
        """
        def distance(x1, y1, x2, y2):
            from math import sqrt
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        distances = []
        for i,row in enumerate(self.board):
            for j,val in enumerate(row):
                if val == False:
                    distances.append((distance(x,y,i,j),i,j))
        if len(distances) == 0:
            return False

        distances.sort(key=lambda x: x[0])
        return distances[0][1:]

    def first_available_move(self):
        """method description
        :param _name_: _explanation
        """
        try:
            return closest_free(self.board, 0, 0)
        except IndexError:
            return False

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

    def get_edges(self,square):
        """method description
        :param _name_: _explanation
        """
        #for square (i,j) returns the 4-tuple of 0-1 for the edges of this square
        # ordered(top,left,right,bottom)
        i,j = square
        i = int(i)
        j = int(j)
        sq_edges = [self.board[i * 2][j],     # top
          self.board[i * 2 + 1][j],      # left
          self.board[i * 2 + 1][j + 1],  # right
          self.board[i * 2 + 2][j]]      # bottom

        return(sq_edges)

    def check_surrounding_squares(self,edge,k):
        """method description
        :param _name_: _explanation
        """
        # will check if any of the surrounding squares has k or more edges
        # (apart from edge), i.e. k=3 will check for squares to be completet with edge
        # will return number of such squares (0-4)
        i,j = edge
        # first trivial cases that can be computed faster without checking the edges
        if k>3: return(0)
        if k<=0:
            if i%2 == 0:
                return(sum([i>0,(i-1)/2+1 < self.nb_cols-1]))
            else:
                return(sum([j>0,j < self.nb_cols - 1]))
        # now all other cases
        num = 0
        if i % 2 == 0:
            # Now it's time to check for new 3-boxes
            # o   o
            #
            # o---o  A new horizontal line can only fill in above
            #        or below
            # o   o
            if i > 0:
                # check above
                sq_edges = self.get_edges(((i-1)/2, j))
                if sum(sq_edges)>= k:
                    num += 1
            if (i-1)/2+1 < self.nb_cols -1:
                # check below
                sq_edges = self.get_edges(((i-1)/2+1, j))
                if sum(sq_edges)>= k:
                    num += 1
        else:
            # Now it's time to check for new boxes
            # o   o   o   A new vertical line can only fill in
            #     |       on the left or right
            # o   o   o
            if j > 0:
                # check left
                sq_edges = self.get_edges(((i-1)/2, j-1))
                if sum(sq_edges)>= k:
                    num += 1

            if j < self.nb_cols - 1:
                # check right
                sq_edges = self.get_edges(((i-1)/2, j))
                if sum(sq_edges)>= k:
                    num += 1
        return(num)
