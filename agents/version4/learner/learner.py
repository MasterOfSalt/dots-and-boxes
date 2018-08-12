import sys
sys.path.append('../..')
from boards.strings_board import Strings_board
from itertools import combinations
import version4.qlearning as qlearning
import numpy as np
RW = 10
gamma = 1
def train(nb_rows,nb_cols):
    board = Strings_board(nb_rows,nb_cols)
    edges = []
    for i, row in enumerate(board.board):
        for j, val in enumerate(row):
            board.board[i][j] = True
            edges.append((i,j))
    for m in range(nb_rows * nb_cols):

        board_states = combinations(edges,m)

        if m==0:    #end states
            board_num = str(qlearning.board2num(board.board))
            max_score = (nb_rows * nb_cols)

            Qedge = [dict()]
            Q = [[dict() for i in range(max_score+1)]]
            for score in range(max_score+1):
                Q[m][score][board_num] = RW*(score-(max_score//2))

        else:
            # initiate row in Q-value lookup table
            Q.append([ dict() for i in range(max_score - int(np.floor(m//4)))])
            Qedge.append(dict())
            for board_state in board_states:
                # construct board from board state

                for edge in board_state:
                    i,j = edge
                    board.board[i][j] = False

                # find out how many squares are already filled
                total_score = max_score - len(board.get_potential_moves())

                # find the best move - it must be the same, regardless of score
                # we will consider it to be total_score
                potential_moves = []

                for i, row in enumerate(board.board):
                    for j, val in enumerate(row):
                        if val == False:
                            gain = board.check_surrounding_squares((i,j),3)
                            # move remembers edge inserted and score gain,
                            potential_moves.append(((i,j), gain))

                # map potential_moves on Q-values
                qmax = -np.inf
                board_num = qlearning.board2num(board.board)
                for move in potential_moves:
                    edge,gain = move
                    edge_num = qlearning.edge2num(edge)
                    if gain:
                        qval = gamma*Q[m-1][total_score+gain][str(board_num + edge_num)]
                    else:
                        qval = -gamma*Q[m-1][0][str(board_num + edge_num)]

                    if qmax < qval:
                        qmax = qval
                        best_edge = edge

                # insert Q-values
                for score_state in range(total_score+1):
                    Q[m][score_state][str(board_num)] = qmax - RW*(total_score-score_state)
                # insert best move
                Qedge[m][str(board_num)] = best_edge

                for edge in board_state:
                    i,j = edge
                    board.board[i][j] = True
    return(Q, Qedge)

def doit(nb_rows,nb_cols):

    Q,Qedge = train(nb_rows,nb_cols)
    f = open('Q_' + str(nb_rows)+ 'x'+ str(nb_cols) + '.txt','w')
    json.dump(Q,f)
    f.close()
    f = open('Qedge_' + str(nb_rows)+ 'x'+ str(nb_cols) + '.txt','w')
    json.dump(Qedge,f)
    f.close()

doit(4,4)
