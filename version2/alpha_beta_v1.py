import sys
max = sys.maxsize
def alphabeta(board,depth,player):
    if depth == 0:
        return (move[0],move[1], board.boxes[1] - board.boxes[0])
    else:
        return maximax(board,depth,player,-max,max)

def done(move):
    return move[0],move[1],1337

def maximax(board, depth, player,alpha,beta,move= (0,0)):
    if depth == 0:
        return done(move)
    move =  ()
    score = -max
    for x, y in board.free_lines():
        current = board.copy()
        if current.fill_line(x, y, player):
            (a,b,current_score) = maximax(current,depth-1,player,alpha,beta,(x,y))
        else:
            (a,b,current_score) = minimin(current,depth-1,player,alpha,beta,(x,y))
        if current_score > score:
            move = (x,y)
            score = current_score
        alpha = bigger(score, alpha)
        if beta <= alpha:
            break
    return (move[0],move[1],score)

def minimin(board, depth,player,alpha,beta,move=(0,0)):
    if depth == 0:
        return done(move)
    move = ()
    score = max
    for x, y in board.free_lines():
        current = board.copy()
        if current.fill_line(x, y, player):
            (a,b,current_score) = minimin(current,depth-1,player,alpha,beta,(x,y))
        else:
            (a,b,current_score) = maximax(current,depth-1,player,alpha,beta,(x,y))
        if current_score < score:
            move = (x,y)
            score = current_score
        beta = smaller(beta, score)
        if beta <= alpha:
            break
    return (move[0],move[1],score)

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def smaller(a,b):
    if a < b:
        return a
    else:
        return b

def swap_player(player):
    if player == 1:
        return 2
    else:
        return 1
