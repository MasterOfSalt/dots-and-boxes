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
    return 0

def find_longest_chain(game):
    longest_chain = 0
    for i in range(1,game.r,2):
        for j in range(1,game.c,2):
            longest_chain = max(longest_chain, longest_chain_from(game, dict(), i, j, 0))
    return longest_chain

def get_chain_count(game):
    chain_count = 0
    for i in range(1,game.r,2):
            if longest_chain_from(game, dict(), i, j, 0) >= 3:
                chain_count += 1
    return chain_count
