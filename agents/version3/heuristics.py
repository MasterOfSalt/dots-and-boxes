from random import randint
def completeBox(board):
    """method description
    :param x: _explanation
    """
    for row in range(board.nb_rows):
        for col in range(board.nb_cols):
            number_of_borders = board.number_of_borders((row,col))
            if sum(number_of_borders) == 3:
                return ([row*2,row*2+1,row*2+1,row*2+2][number_of_borders.index(0)],[col,col,col+1,col][number_of_borders.index(0)])
    return(False)
def find_good_move(board):
    """method description
    :param x: _explanation
    """
    move = completeBox(board)
    moves = []
    primary_moves = []
    if move:
        return(move)
    for i, row in enumerate(board.board):
        for j, val in enumerate(row):
            newmove = (i,j)
            if not val:
                moves.append((i,j))
                if not board.find_boxes(newmove):
                    primary_moves.append(newmove)
    if not moves:
        return(False)
    else:
        if primary_moves:
            return(primary_moves[randint(0,len(primary_moves)-1)])
        else:
            return(moves[randint(0,len(moves)-1)])
