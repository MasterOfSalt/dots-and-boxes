"""
    wi stands for the number of wins for the node considered after the i-th move
    ni stands for the number of simulations for the node considered after the i-th move
    Ni stands for the total number of simulations after the i-th move
    c is the exploration parameter—theoretically equal to √2; in practice usually chosen empirically

"""


class Node():
	def __init__(self,move,wins,sims,parent=None):
        self.wins = wins
        self.simulations = sims
        self.move = move
        self.children = []

	def update(self,win):
        if win:
            self.wins+=1
		self.simulations+=1
    def add_child(self,child):
        children.append(child)
    def save_to_file(self):
        for child in children:
            if child.children empty:
                write(move,wins,sims,{})
            else:
                write(move,wins,sims,child.save_to_file())
