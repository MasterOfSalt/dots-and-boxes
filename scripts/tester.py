from treeparser import TreeParser

tp = TreeParser(1,9)
tp.process_games()
print(tp.get_best_move(tp.tree['nodes'])['children'])
print(tp.set_move(tp.tree['nodes'],"1,1,v")['children'])
