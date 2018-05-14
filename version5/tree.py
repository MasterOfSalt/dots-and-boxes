class Tree():
	def __init__(self, nb_rows,nb_cols):
        self.children = []
    def fill(self):
        #read from file
        #add children

    def getchildren(self,state):
        i = 0
        children = []
        while i<0 len(state):
            children = state.children
            i+=1
        return children
	def update(self,moves,win):
		for move in moves:

	def next_move(self,state):
		best_move = dummy_move
		for child in children:
			if child.wins/child.simulations > best_move.wins/best_move.simulations:
				best_move = child
		return best_move

	def save_to_file(self):
		for child in children:
			child.save_to_file()

	def read_from_file(self):
		#add child from file
