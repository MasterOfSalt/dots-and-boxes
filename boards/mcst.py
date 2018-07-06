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



# add_game(['1,2,h','1,1,v','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h','1,3,h'],1)
