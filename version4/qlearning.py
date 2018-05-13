import json
import version3.heuristics as heuristics
import numpy as np

BOARD_SIZE=4
WEIGHTS = np.array([2**i for i in range(2*BOARD_SIZE*(BOARD_SIZE-1))])

def bot2_move(board,Qedge,k):
    # last k moves are best possible, the rest is played by always4never3 strategy

    m = 0
    for i, row in enumerate(board.board):
        for j, val in enumerate(row):
            if val == False: m += 1

    if m < k:
        board_num = board2num(board)
        move = Qedge[m][str(board_num)]
    else:
        move = heuristics.always4never3(board)

    return(move)

def board2num(board):
    b = list(sum(board,[]))
    num = sum(WEIGHTS[i] for i in range(len(WEIGHTS))  if b[i])
    return num

def bot2_load(k):
    #f = open('Qedge_' + str(k)+ '_'+ str(BOARD_SIZE) + '.txt','r')
    f = open('Qedge_10_4.txt','r')
    Qedge = json.load(f)
    f.close()

    return(Qedge)
