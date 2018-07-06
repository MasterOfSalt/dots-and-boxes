import json,os
import json
import sys
import glob
import errno
import os
import sys
import glob
import errno

class MonteCarloSearchTree:
    def __init__(self,n,m):
        self.dimensions = 'version5/'+str(n) + 'x' +str(m)
        self.tree = {}
        if os.path.isfile(self.dimensions+'/tree.data'):
            file = open(self.dimensions+'/tree.data')
            self.tree = json.loads(file.read())
            file.close()
        else:
            self.tree['nodes'] = []
            init = json.dumps(self.tree)
            os.makedirs(self.dimensions)
            os.makedirs(self.dimensions+'/games')
            os.makedirs(self.dimensions+'/games/processed')
            os.makedirs(self.dimensions+'/games/unprocessed')
            file = open(self.dimensions+'/tree.data', 'a+')
            file.write(init)
            file.close()

    def explore_new_nodes(self,l,nodes,win):
        for el in l:
            if win:
                nodes.append({
                    'wins': 1,
                    'plays': 1,
                    'move': el,
                    'children':[]
                })
                win = False
            else:
                nodes.append({
                    'wins': 0,
                    'plays': 1,
                    'move': el,
                    'children':[]
                })
                win = True
            nodes = nodes[0]['children']

    def get_best_move(self,nodes):
        winrate = -1
        next_move = False
        for node in nodes:
            if node['wins']/node['plays'] > winrate:
                next_move = node
        return next_move

    def fill_line(self,nodes,move):
        for node in nodes:
            if node['move'] == move:
                return node
        return False


    def add_game(self,l,winner):
        go = True
        if(winner == 1):
            win = True
        if(winner == 2):
            win = False
        if(winner == 0):
            go = False
            nodes = self.tree['nodes']
            while(len(l)>0 and go):
                done = False
                el = l.pop(0)
                for node in nodes:
                    if node['move'] == el:
                        node['plays'] += 1
                        nodes = node['children']
                        done = True
                        break
                if not done:
                    self.explore_new_nodes([el] + l,nodes,win)
                    break
            with open(self.dimensions+'/tree.data', 'w') as outfile:
                json.dump(self.tree, outfile)

        nodes = self.tree['nodes']
        while(len(l)>0 and go):
            done = False
            el = l.pop(0)
            for node in nodes:
                if node['move'] == el:
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
                self.explore_new_nodes([el] + l,nodes,win)
                break
        with open(self.dimensions+'/tree.data', 'w') as outfile:
            json.dump(self.tree, outfile)


    def process_games(self):
        path = self.dimensions + '/games/unprocessed/*.json'
        files = glob.glob(path)
        for name in files:
            try:
                with open(name,'r') as f:
                    basicList = json.load(f)
                    base = os.path.basename(name)
                    winner = int(base.split('_')[1].split('.')[0])
                    self.add_game(basicList,winner)
                os.rename(name, self.dimensions + "/games/processed/"+base)
            except IOError as exc:
                if exc.errno != errno.EISDIR:
                    raise



# add_game(['1,2,h','1,1,v','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h'],1)
