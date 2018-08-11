"""
from:"Chapter 16: Dots-and-Boxes", Winning Ways for your Mathematical Plays, Volume 2: Games in Particular, Academic Press, pp. 507–550.
Dots and Boxes has a dual graph form called "Strings-and-Coins".
 This game is played on a network of coins (vertices) joined by strings (edges).
 Players take turns cutting a string.
 When a cut leaves a coin with no strings, the player "pockets" the coin and takes another turn.
 The winner is the player who pockets the most coins.
 Strings-and-Coins can be played on an arbitrary graph
"""
import numpy as np

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
        playagain = False
        self.board[i,j] = player
        vertical = i%2 > j%2
        if vertical:
            if self.calc_score_for_set_line(player, i, j-1):
                self.score[player-1] += 1
                playagain = True
            if self.calc_score_for_set_line(player, i, j+1):
                self.score[player-1] += 1
                playagain = True
        else:
             if self.calc_score_for_set_line(player, i-1, j):
                 self.score[player-1] += 1
                 playagain = True
             if self.calc_score_for_set_line(player, i+1, j):
                 self.score[player-1] += 1
                 playagain = True
        return playagain

    def calc_score_for_set_line(self, player, i, j):
        if (i and i < self.r) and (j and j < self.c):
            return self.board[i-1, j] and self.board[i+1, j] and self.board[i, j-1] and self.board[i, j+1]
        else:
            return False

    def longest_chain_from(self, visited, i, j, length):
        place = str(i) + str(j)
        if not (i > 0 and i < self.r and j > 0 and j < self.c) or place in visited:
            return length
        visited[place] = True
        # find openings
        horizontal, vertical = self.board[i-1, j] and self.board[i+1, j], self.board[i, j-1] and self.board[i, j+1]
        # follow each opening and return length
        if horizontal:
            return max(longest_chain_from(visited, i, j-2, length+1), longest_chain_from( visited, i, j+2, length+1))
        elif vertical:
            return max(longest_chain_from(visited, i-2, j, length+1), longest_chain_from(visited, i+2, j, length+1))
        return 0

    def find_longest_chain(self):
        longest_chain = 0
        for i in range(1,self.r,2):
            for j in range(1,self.c,2):
                longest_chain = max(longest_chain, longest_chain_from(dict(), i, j, 0))
        return longest_chain

    def get_chain_count(self):
        chain_count = 0
        for i in range(1,self.r,2):
                if longest_chain_from(dict(), i, j, 0) >= 3:
                    chain_count += 1
        return chain_count
