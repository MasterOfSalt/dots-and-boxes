import json,os
import json
import sys
import glob
import errno
import os
import sys
import glob
import errno
from os import path

class MonteCarloSearchTree:
    
    def __init__(self,n,m):
        self.dimensions = '../data/'+str(n) + 'x' +str(m)
        self.tree = {}
        if os.path.isfile(self.dimensions+'/tree.data'):

            file = open(self.dimensions+'/tree.data')
            self.tree = json.loads(file.read())
            file.close()
        else:
            self.tree['nodes'] = []
            init = json.dumps(self.tree)
            os.makedirs(self.dimensions, exist_ok=True)
            os.makedirs(self.dimensions+'/processed', exist_ok=True)
            os.makedirs(self.dimensions+'/unprocessed', exist_ok=True)
            file = open(self.dimensions+'/tree.data', 'a+')
            file.write(init)
            file.close()

        """method description
        Indien de game een win was:
            
        """     
    def explore_new_nodes(self,nodelist,nodes,win):
        for move in nodelist:
            if win:
                nodes.append({
                    'wins': 1,
                    'plays': 1,
                    'move': move,
                    'children':[]
                })
                win = False
            else:
                nodes.append({
                    'wins': 0,
                    'plays': 1,
                    'move': move,
                    'children':[]
                })
                win = True
            nodes = nodes[0]['children']

    def get_best_move(self,nodes):
        winrate = -1
        next_move = False
        for node in nodes:
            if node['wins']/node['plays'] > winrate:
                next_move = node['move']
        return next_move

    def fill_line(self,nodes,move):
        for node in nodes:
            if node['move'] == move:
                return node
        return False


    def add_game(self,nodelist,winner):
        go = True
        if(winner == 1):
            win = True
        if(winner == 2):
            win = False
        if(winner == 0):
            go = False
            nodes = self.tree['nodes']
            while(len(nodelist)>0 and go):
                done = False
                move = nodelist.pop(0)
                for node in nodes:
                    if node['move'] == el:
                        node['plays'] += 1
                        nodes = node['children']
                        done = True
                        break
                if not done:
                    self.explore_new_nodes([move] + nodelist,nodes,win)
                    break
            '''  with open(self.dimensions+'/tree.data', 'w') as outfile:
                    json.dump(self.tree, outfile)
            '''

        nodes = self.tree['nodes']
        while(len(nodelist)>0 and go):
            done = False
            move = nodelist.pop(0)
            for node in nodes:
                if node['move'] == move:
                    node['plays'] += 1
                    if win:
                        node['wins'] += 1
                        win = False
                    else:
                        win = True
                    nodes = node['children']
                    done = True
                    break
            if not done:
                self.explore_new_nodes([move] + nodelist,nodes,win)
                break
            '''             with open(self.dimensions+'/tree.data', 'w') as outfile:
                json.dump(self.tree, outfile)
            '''

    def process_games(self):
        path = self.dimensions + '/unprocessed/*.json'
        files = glob.glob(path)
        for name in files:
            try:
                with open(name,'r') as f:
                    print(name)
                    basicList = json.load(f)
                    base = os.path.basename(name)
                    winner = int(base.split('_')[1].split('.')[0])
                    self.add_game(basicList,winner)
                os.rename(name, self.dimensions + "/processed/"+base)

            except IOError as exc:
                if exc.errno != errno.EISDIR:
                    raise
                    
        with open(self.dimensions+'/tree.data', 'w') as outfile:
            json.dump(self.tree, outfile)


# add_game(['1,2,h','1,1,v','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h'],1)
