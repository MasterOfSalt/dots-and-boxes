import sys


from boards.mcst import MonteCarloSearchTree

# main
param_1= sys.argv[1]
param_2= sys.argv[2]

mt = MonteCarloSearchTree(param_1,param_2)
# mt.process_games()
# mt.parentPlays()
print(mt.get_best_move(mt.tree["nodes"]))
