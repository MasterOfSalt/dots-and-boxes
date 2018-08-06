import json
import version3.heuristics as heuristics
import numpy as np

BOARD_SIZE=4
WEIGHTS = np.array([2**i for i in range(2*BOARD_SIZE*(BOARD_SIZE-1))])

def board2num(board):
    b = list(sum(board,[]))
    num = sum(WEIGHTS[i] for i in range(len(WEIGHTS))  if b[i])
    return num
def edge2num(edge):
    i,j = edge
    num = int(np.floor(i//2)*(2*BOARD_SIZE-1) + j)
    if i % 2 == 1:
        num += BOARD_SIZE-1
    return(WEIGHTS[num])
def loadfile(k):
    #f = open('Qedge_' + str(k)+ '_'+ str(BOARD_SIZE) + '.txt','r')
    f = open('Qedge_10_4.txt','r')
    Qedge = json.load(f)
    f.close()
    return(Qedge)
