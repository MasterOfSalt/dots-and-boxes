from random import randint

def get_first_completing_move(board):
    """method description
    :param x: _explanation
    """
    # returns completing move, if exists
    # otherwise returns False
    #adding some text
    for i in range(board.nb_rows-1):
        for j in range(board.nb_rows-1):
            sq_edges = board.get_edges((i,j))
            if sum(sq_edges) == 3:
                ind = sq_edges.index(0)
                xc = [i*2,i*2+1,i*2+1,i*2+2]
                yc = [j,j,j+1,j]
                return (xc[ind],yc[ind])
    return(False)

def always4never3(board):
    """method description
    :param x: _explanation
    """
    move = get_first_completing_move(board)
    if move:
        return(move)
    potential_moves = []
    potential_moves_not3 = []
    for i, row in enumerate(board.board):
        for j, val in enumerate(row):
            if val == False:
                potential_moves.append((i,j))
                tmp = board.check_surrounding_squares((i,j),2)
                if not tmp: potential_moves_not3.append((i,j))
    if not potential_moves:
        return(False)
    else:
        if potential_moves_not3:
            return(potential_moves_not3[randint(0,len(potential_moves_not3)-1)])
        else:
            return(potential_moves[randint(0,len(potential_moves)-1)])
