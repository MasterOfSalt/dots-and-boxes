inf = float("inf")

def alphabeta(board, depth=10, alpha = -inf, beta = inf, is_max = True, player = True, move = (0,0)):
    children = board.free_lines()
    if len(children) == 0 or depth == 0:
        #print(move)
        return (move[0],move[1], board.boxes[1] - board.boxes[0])
    if is_max:
        best_move =  ()
        best_score = -inf
        best_move_x = -1
        best_move_y = -1
        for x, y in children:
            current = board.copy()
            turn = current.fill_line(x, y, player)
            (a,b,score) = alphabeta(current, depth - 1, alpha, beta, turn, player, (x,y))
            if score > best_score:
                best_move = (x,y)
                best_move_x = x
                best_move_y = y
                best_score = score
            alpha = max(best_score, alpha)
            if beta <= alpha:
                break
        return (best_move_x,best_move_y,best_score)
    else:
        worse_move = ()
        worse_score = inf
        best_move_x = -1
        best_move_y = -1
        for x, y in children:
            current = board.copy()
            turn = current.fill_line(x, y, swap_player(player))
            (a,b,score) = alphabeta(current, depth - 1, alpha, beta, not turn, player, (x,y))
            if (score) < worse_score:
                best_move_x = x
                best_move_y = y
                worse_move = (x,y)
                worse_score = score
            beta = min(beta, worse_score)
            if beta <= alpha:
                break
        return (best_move_x,best_move_y,worse_score)

def swap_player(player):
    if player == 1:
        return 2
    else:
        return 1
