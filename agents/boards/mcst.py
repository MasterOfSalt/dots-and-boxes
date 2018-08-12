import json,os
import json
import sys
import glob
import errno
import os
import sys
import glob
import errno
from math import sqrt
from math import log
import cmath
from os import path
import itertools as it
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
    def explore_new_nodes_no_winner(self,nodelist,nodes):
        for move in nodelist:
            nodes.append({
                    'wins': 0,
                    'plays': 1,
                    'move': move,
                    'children':[]
                })
            nodes = nodes[0]['children']
    def get_best_move(self,nodes):
        winrate = -1
        next_move = False

        for node in nodes:
            print (node['plays'])
            if 'parentPlays' in node:
                if node['plays'] is not 0:
                    print (node['parentPlays'])
                    print("YES")
                    if (isinstance(cmath.sqrt(2*log(node['parentPlays']/node['plays'])), complex)):
                        print("kak")
                    else:
                        if (node['wins']/node['plays'] + cmath.sqrt(2*log(node['parentPlays']/node['plays']))) > winrate:
                            next_move = node['move']
                        return next_move
            else:
                if (node['wins']/node['plays']) > winrate:
                    next_move = node['move']
                return next_move

    """ x = node['wins']/node['plays'] + sqrt(2*log(node['plays']/[node['plays']]))"""

    def fill_line(self,nodes,move):
        for node in nodes:
            if node['move'] == move:
                return node
        return False

    def add_sequence_to_tree(self,last,combo,winner):
        nodes = self.tree['nodes']
        found = True
        while(len(combo)>0 and found):
            found = False
            move = combo.pop(0)
            for node in nodes:
                if node['move'] == move:
                    nodes = node['children']
                    found = True
                    break
        if len(combo)>0:
            for move in combo:
                nodes.append({
                        'wins': 0,
                        'plays': 0,
                        'move': move,
                        'children':[]
                    })
                nodes = nodes[0]['children']
        if(winner == 1 and (len(combo) + 1)%2 == 0):
            nodes.append({
                    'wins': 0,
                    'plays': 1,
                    'move': last,
                    'children':[]
                })
        if(winner == 1 and (len(combo) + 1)%2 != 0):
            nodes.append({
                    'wins': 1,
                    'plays': 1,
                    'move': last,
                    'children':[]
                })
        if(winner == 2 and (len(combo) + 1)%2 == 0):
            nodes.append({
                    'wins': 1,
                    'plays': 1,
                    'move': last,
                    'children':[]
                })
        if(winner == 2 and (len(combo) + 1)%2 != 0):
            nodes.append({
                    'wins': 0,
                    'plays': 1,
                    'move': last,
                    'children':[]
                })
        if(winner == 0):
            nodes.append({
                    'wins': 0,
                    'plays': 1,
                    'move': last,
                    'children':[]
                })

    def add_all_sequences(self,my_list,winner):
        subs = [[]]
        for i in range(len(my_list)):
            n = i+1
            while n <= len(my_list):
                sub = my_list[i:n]
                subs.append(sub)
                n += 1
        for steak_cheese in subs:
            if len(steak_cheese) > 1:
                last = steak_cheese.pop()
                combos = list(it.permutations(steak_cheese, len(steak_cheese)))
                for combo in combos:
                    self.add_sequence_to_tree(last,list(combo),winner)



    def add_game(self,nodelist,winner):
        #self.add_all_sequences(nodelist,winner)
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
                    if node['move'] == move:
                        node['plays'] += 1
                        nodes = node['children']
                        done = True
                        break
                if not done:
                    self.explore_new_nodes_no_winner([move] + nodelist,nodes)
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

            except:
                print("mislukt")
                continue

        with open(self.dimensions+'/tree.data', 'w') as outfile:
            json.dump(self.tree, outfile)
    def addToChildren(self,nodes,value):
        for node in nodes:
            node['parentPlays'] = value
            plays = node['plays']
            if node['children'] != []:
                self.addToChildren(node['children'],plays)

    def parentPlays(self):
        for node in self.tree['nodes']:
            plays = node['plays']
            if node['children'] != []:
                self.addToChildren(node['children'],plays)
        with open(self.dimensions+'/tree.data', 'w') as outfile:
            json.dump(self.tree, outfile)



# add_game(['1,2,h','1,1,v','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h'],1)
