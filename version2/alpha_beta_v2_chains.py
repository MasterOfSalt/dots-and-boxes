import sys

def longest_chain_from(game, visited, i, j, length):
    place = str(i) + str(j)
    if not (i > 0 and i < game.r and j > 0 and j < game.c) or place in visited:
        return length
    visited[place] = True
    # find openings
    horizontal, vertical = game.board[i-1, j] and game.board[i+1, j], game.board[i, j-1] and game.board[i, j+1]
    # follow each opening and return length
    if horizontal:
        return max(longest_chain_from(game, visited, i, j-2, length+1), longest_chain_from(game, visited, i, j+2, length+1))
    elif vertical:
        return max(longest_chain_from(game, visited, i-2, j, length+1), longest_chain_from(game, visited, i+2, j, length+1))

def find_longest_chain(game):
    # for each square in game
    longest_chain = 0
    for i in range(1,game.r,2):
        for j in range(1,game.c,2):
            # find biggest chain starting in square
            longest_chain = max(longest_chain, longest_chain_from(game, dict(), i, j, 0))
    return longest_chain

def get_chain_count(game):
    # for each square in game
    chain_count = 0
    for i in range(1,game.r,2):
        for j in range(1,game.c,2):
            # find biggest chain starting in square
            if longest_chain_from(game, dict(), i, j, 0) >= 3:
                chain_count += 1
    return chain_count

import sys
max = sys.maxsize
def alphabeta(board,depth,player):
    """method description
    :param x: _explanation
    """
    return maximax(board,depth,player,-max,max)

def done(move):
    """method description
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
        if current.fill_line(x, y, player):
            (a,b,current_score) = maximax(current,depth-1,player,alpha,beta,(x,y))
        else:
            (a,b,current_score) = minimin(current,depth-1,player,alpha,beta,(x,y))
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
