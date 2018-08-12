"""
Pseudocode from https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
01 function alphabeta(node, depth, α, β, maximizingPlayer) is
02     if depth = 0 or node is a terminal node then
03         return the heuristic value of node
04     if maximizingPlayer then
05         v := -∞
06         for each child of node do
07             v := max(v, alphabeta(child, depth – 1, α, β, FALSE))
08             α := max(α, v)
09             if β ≤ α then
10                 break (* β cut-off *)
11         return v
12     else
13         v := +∞
14         for each child of node do
15             v := min(v, alphabeta(child, depth – 1, α, β, TRUE))
16             β := min(β, v)
17             if β ≤ α then
18                 break (* α cut-off *)
19         return v
"""
import sys
max = sys.maxsize
maxstates = []
minstates = []
visited_states = 0

def add(x):
    global visited_states
    visited_states += x

def init():
    global visited_states    # Needed to modify global copy of globvar
    visited_states = 0

def alphabeta(board,depth,player):
    """method description
    :param x: _explanation
    """
    maxstates = []
    minstates = []
    init()
    return maximax(board,depth,player,-max,max)

def done(move):
    """finishing statement
    :param x: _explanation
    """
    return move[0],move[1],1337

def maximax(board, depth, player,alpha,beta,move=(0,0)):
    """method description
    :param x: _explanation
    """
    if depth == 0:
        return done(move)
    score = board.boxes[player-1]
    for x, y in board.free_lines():
        current = board.copy()
        for (a1,b1) in maxstates:
            if a1 == current:
                add(1)
                return (x,y,b1)
        if current.fill_line(x, y, player):
            (a,b,current_score) = maximax(current,depth-1,player,alpha,beta,(x,y))
        else:
            (a,b,current_score) = minimin(current,depth-1,player,alpha,beta,(x,y))
        maxstates.append((current,current_score))
        if current_score > score:
            move = (x,y)
            score = current_score
        alpha = bigger(score, alpha)
        #print (score)
        if beta <= alpha:
            break
    return (move[0],move[1],score)

def minimin(board, depth,player,alpha,beta,move=(0,0)):
    """method description
    :param x: _explanation
    """
    if depth == 0:
        return done(move)
    score = board.max_points()
    for x, y in board.free_lines():
        current = board.copy()
        for (a1,b1) in minstates:
            if a1 == current:
                add(1)
                return (x,y,b1)
        if current.fill_line(x, y, player):
            (a,b,current_score) = minimin(current,depth-1,player,alpha,beta,(x,y))
        else:
            (a,b,current_score) = maximax(current,depth-1,player,alpha,beta,(x,y))
        minstates.append((current,current_score))
        if current_score < score:
            move = (x,y)
            score = current_score
        beta = smaller(beta, score)
        if beta <= alpha:
            break
        #print (score)
    return (move[0],move[1],score)

def bigger(a,b):
    """method description
    :param x: _explanation
    """
    if a > b:
        return a
    else:
        return b

def smaller(a,b):
    """method description
    :param x: _explanation
    """
    if a < b:
        return a
    else:
        return b

def swap_player(player):
    """method description
    :param x: _explanation
    """
    if player == 1:
        return 2
    else:
        return 1
