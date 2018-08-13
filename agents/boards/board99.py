import logging
from timeit import Timer
import resource
import sys
sys.setrecursionlimit(1500)

logger = logging.getLogger(__name__)


class Board:

    def __init__(self,nb_rows,nb_cols):
        self.nb_rows = nb_rows
        self.nb_cols = nb_cols
        rows = []
        for ri in range(nb_rows + 1):
            columns = []
            for ci in range(nb_cols + 1):
                columns.append({"v":0, "h":0})
            rows.append(columns)
        self.cells = rows

    def free_lines(self):
        free_lines = []
        used_lines = []
        
        for ri in range(len(self.cells)):
            row = self.cells[ri]

            for ci in range(len(row)):
                cell = row[ci]
                if ri < (len(self.cells) - 1) and cell["v"] == 0:
                    free_lines.append((ri, ci, "v"))
                if ci < (len(row) - 1) and cell["h"] == 0:
                    free_lines.append((ri, ci, "h"))
                    
        return free_lines
    

    def used_lines(self):
        free_lines = []
        used_lines = []
        
        for ri in range(len(self.cells)):
            row = self.cells[ri]

            for ci in range(len(row)):
                cell = row[ci]
                    
                if ri < (len(self.cells) - 1) and cell["v"] != 0:
                    used_lines.append((ri, ci, "v"))
                if ci < (len(row) - 1) and cell["h"] != 0:
                    used_lines.append((ri, ci, "h"))
                    
        return used_lines

  
    def chain_neighbors(self,line, visited_lines):
        global current_chain_length
        if line not in visited_lines:
            used_lines = self.used_lines()

            r, c, o = line
            line_horizontal_left_up = None
            line_horizontal_left_down = None
            line_horizontal_right_up = None
            line_horizontal_right_down = None
            line_vertical_up = None
            line_vertical_down = None
            line_horizontal_left = None
            line_horizontal_right = None
            line_vertical_left_up = None
            line_vertical_left_down = None
            line_vertical_right_up = None
            line_vertical_right_down = None

            if o == "v":
                line_horizontal_left_up = r, c-1, "h"
                line_horizontal_left_down = r+1, c-1, "h"
                line_horizontal_right_up = r, c, "h"
                line_horizontal_right_down = r+1, c, "h"
                line_vertical_up = r-1, c, "v"
                line_vertical_down = r+1, c, "v"
            elif o == "h":
                line_horizontal_left = r, c-1, o
                line_horizontal_right = r, c+1, o
                line_vertical_left_up = r-1, c, "v"
                line_vertical_left_down = r, c, "v"
                line_vertical_right_up = r-1, c+1, "v"
                line_vertical_right_down = r, c+1, "v"


            visited_lines.append(line)
            if line_horizontal_left_up in used_lines and line_horizontal_left_up not in visited_lines:
                current_chain_length += 1
                self.chain_neighbors(line_horizontal_left_up, visited_lines)
                visited_lines.append(line_horizontal_left_up)
                
            if line_horizontal_left_down in used_lines and line_horizontal_left_down not in visited_lines:
                current_chain_length += 1
                self.chain_neighbors(line_horizontal_left_down, visited_lines )
                visited_lines.append(line_horizontal_left_down)
                
            if line_horizontal_right_up in used_lines and line_horizontal_right_up not in visited_lines:
                current_chain_length += 1
                self.chain_neighbors(line_horizontal_right_up, visited_lines )
                visited_lines.append(line_horizontal_right_up)
                
            if line_horizontal_right_down in used_lines and line_horizontal_right_down not in visited_lines:
                current_chain_length += 1
                self.chain_neighbors(line_horizontal_right_down, visited_lines )
                visited_lines.append(line_horizontal_right_down)
                
            if line_vertical_up in used_lines and line_vertical_up not in visited_lines:
                current_chain_length += 1
                self.chain_neighbors(line_vertical_up, visited_lines )
                visited_lines.append(line_vertical_up)
                
            if line_vertical_down in used_lines and line_vertical_down not in visited_lines:
                current_chain_length += 1
                self.chain_neighbors(line_vertical_down, visited_lines )
                visited_lines.append(line_vertical_down)
                
            if line_horizontal_left in used_lines and line_horizontal_left not in visited_lines:
                current_chain_length += 1
                self.chain_neighbors(line_horizontal_left, visited_lines )
                visited_lines.append(line_horizontal_left)
                
            if line_horizontal_right in used_lines and line_horizontal_right not in visited_lines:
                current_chain_length += 1
                self.chain_neighbors(line_horizontal_right, visited_lines )
                visited_lines.append(line_horizontal_right)
                
            if line_vertical_left_up in used_lines and line_vertical_left_up not in visited_lines:
                current_chain_length += 1
                self.chain_neighbors(line_vertical_left_up, visited_lines )
                visited_lines.append(line_vertical_left_up)
                
            if line_vertical_left_down in used_lines and line_vertical_left_down not in visited_lines:
                current_chain_length += 1
                self.chain_neighbors(line_vertical_left_down, visited_lines )
                visited_lines.append(line_vertical_left_down)
                
            if line_vertical_right_up in used_lines and line_vertical_right_up not in visited_lines:
                current_chain_length += 1
                self.chain_neighbors(line_vertical_right_up, visited_lines )
                visited_lines.append(line_vertical_right_up)
                
            if line_vertical_right_down in used_lines and line_vertical_right_down not in visited_lines:
                current_chain_length += 1
                self.chain_neighbors(line_vertical_right_down, visited_lines )
                visited_lines.append(line_vertical_right_down)

        else:
            """print ("In visited lines")"""
            
    current_chain_length = 0
    twee_buren_geadd2 = 0
    chain_count = 0

    def is_chain(self):
        global current_chain_length
        global chain_count
        visited_lines = []
        self.reset_chain_counter()
        used_lines = self.used_lines()
        """print("----------------------------CHAIN ANALYSIS----------------------------")"""

        for line in used_lines:
            current_chain_length = 1
            chain_count = 0
            """print("LINE IS:"+str(line))"""

            self.chain_neighbors(line, visited_lines)
            if current_chain_length >= 3:    
                self.chain_counter()
                """print("EUREKA chain ++")"""
                
            """print('\n')
            print("USED_LINES: "+str(used_lines))
            print("VISITED_LINES: "+str(visited_lines))
            print('\n')
            print("NEW Chain count: "+str(self.chain_count))
        
        print("----------------------------end----------------------------")"""

    def chain_counter(self):
        global chain_count
        self.chain_count = self.chain_count+1    
        
    def reset_chain_counter(self):
        global chain_count
        self.chain_count = 0    
        
    def set_twee_buren(self):
        global twee_buren_geadd2
        self.twee_buren_geadd2 = 1    
        
    def reset_twee_buren(self):
        global twee_buren_geadd2
        self.twee_buren_geadd2 = 0    
        
    def print_twee_buren(self):
        global twee_buren_geadd2
        print (self.twee_buren_geadd2) 
        
    def print_count(self):
        global chain_count
        print ("CHAINS: "+str(self.chain_count)) 
        
    def return_twee_buren(self):
        global twee_buren_geadd2
        return (self.twee_buren_geadd2) 
        
    def count_chains(self):
        t = Timer(lambda: self.is_chain())
        print("")
        print ("Timeit chaincounter: ")
        print (t.timeit(number=1))
        global chain_count
        self.is_chain()
        
        
    def fill_line(self,row,column,orientation,player):
        self.cells[row][column][orientation] = player
        
        

    
    def chaining(self,line,visited_lines,used_lines,simulated_lines):
        print("Chaining started")
        global twee_buren_geadd
        global current_chain_length
        r, c, o = line
        line_horizontal_left_up = None
        line_horizontal_left_down = None
        line_horizontal_right_up = None
        line_horizontal_right_down = None
        line_vertical_up = None
        line_vertical_down = None
        line_horizontal_left = None
        line_horizontal_right = None
        line_vertical_left_up = None
        line_vertical_left_down = None
        line_vertical_right_up = None
        line_vertical_right_down = None
        line_vertical_right = None
        line_vertical_left = None
        line_horizontal_up = None
        line_horizontal_down = None

        chained_lines = []
        
        if o == "v":
            line_horizontal_left_up = r, c-1, "h"
            line_horizontal_left_down = r+1, c-1, "h"
            line_horizontal_right_up = r, c, "h"
            line_horizontal_right_down = r+1, c, "h"
            line_vertical_up = r-1, c, "v"
            line_vertical_down = r+1, c, "v"
            line_vertical_left = r, c-1, "v"
            line_vertical_right = r, c+1, "v"
        elif o == "h":
            line_horizontal_left = r, c-1, o
            line_horizontal_right = r, c+1, o
            line_vertical_left_up = r-1, c, "v"
            line_vertical_left_down = r, c, "v"
            line_vertical_right_up = r-1, c+1, "v"
            line_vertical_right_down = r, c+1, "v"
            line_horizontal_up = r-1, c, "h"
            line_horizontal_down = r+1, c, "h"
            
                            
        if o == "v" and line not in chained_lines and line not in visited_lines:
            """if line has 1 ontbrekende buur"""
            if (line_vertical_right in used_lines or line_vertical_right in simulated_lines) and (line_horizontal_right_up in used_lines or line_horizontal_right_up in simulated_lines) and (line_horizontal_right_down not in used_lines and line_horizontal_right_down not in simulated_lines):
                simulated_lines.append(line_horizontal_right_down)
                chained_lines.append(line_horizontal_right_down)
                current_chain_length += 1
                print("1")
                self.chaining(line_horizontal_right_down, visited_lines, used_lines, simulated_lines)
            elif (line_vertical_right in used_lines or line_vertical_right in simulated_lines) and (line_horizontal_right_down in used_lines or line_horizontal_right_down in simulated_lines) and (line_horizontal_right_up not in used_lines and line_horizontal_right_up not in simulated_lines):
                simulated_lines.append(line_horizontal_right_up)
                chained_lines.append(line_horizontal_right_up)
                current_chain_length += 1
                self.chaining(line_horizontal_right_up, visited_lines, used_lines, simulated_lines) 
            elif (line_horizontal_right_up in used_lines or line_horizontal_right_up in simulated_lines) and (line_horizontal_right_down in used_lines or line_horizontal_right_down in simulated_lines) and (line_vertical_right not in used_lines and line_vertical_right not in simulated_lines):
                simulated_lines.append(line_vertical_right)
                chained_lines.append(line_vertical_right)
                current_chain_length += 1
                print("2")
                self.chaining(line_vertical_right, visited_lines, used_lines, simulated_lines) 
            elif (line_vertical_left in used_lines or line_vertical_left in simulated_lines) and (line_horizontal_left_down in used_lines or line_horizontal_left_down in simulated_lines) and (line_horizontal_left_up not in used_lines and line_horizontal_left_up not in simulated_lines):
                simulated_lines.append(line_horizontal_left_up)
                chained_lines.append(line_horizontal_left_up)
                current_chain_length += 1
                print("3")
                self.chaining(line_horizontal_left_up, visited_lines, used_lines, simulated_lines) 
            elif (line_vertical_left in used_lines or line_vertical_left in simulated_lines) and (line_horizontal_left_up in used_lines or line_horizontal_left_up in simulated_lines) and (line_horizontal_left_down not in used_lines and line_horizontal_left_down not in simulated_lines):
                simulated_lines.append(line_horizontal_left_down)
                chained_lines.append(line_horizontal_left_down)
                current_chain_length += 1
                print("4")
                self.chaining(line_horizontal_left_down, visited_lines, used_lines, simulated_lines)  
            elif (line_horizontal_left_down in used_lines or line_horizontal_left_down in simulated_lines) and (line_horizontal_left_up in used_lines or line_horizontal_left_up in simulated_lines) and (line_vertical_left not in used_lines and line_vertical_left not in simulated_lines):
                simulated_lines.append(line_vertical_left)
                chained_lines.append(line_vertical_left)
                current_chain_length += 1
                print("5")
                self.chaining(line_vertical_left, visited_lines, used_lines, simulated_lines) 
                
        elif o =="h" and line not in chained_lines and line not in visited_lines:
            if (line_horizontal_up in used_lines or line_horizontal_up in simulated_lines) and (line_vertical_left_up in used_lines and line_vertical_left_up in simulated_lines) and (line_vertical_right_up not in used_lines or line_vertical_right_up not in simulated_lines):
                simulated_lines.append(line_vertical_right_up)
                chained_lines.append(line_vertical_right_up)
                current_chain_length += 1
                print("6")
                self.chaining(line_vertical_right_up, visited_lines, used_lines, simulated_lines) 
            elif (line_horizontal_up in used_lines or line_horizontal_up in simulated_lines) and (line_vertical_right_up in used_lines and line_vertical_right_up in simulated_lines) and (line_vertical_left_up not in used_lines or line_vertical_left_up not in simulated_lines):
                simulated_lines.append(line_vertical_left_up)
                chained_lines.append(line_vertical_left_up)
                current_chain_length += 1
                print("7")
                self.chaining(line_vertical_left_up, visited_lines, used_lines, simulated_lines) 
            elif (line_vertical_left_up in used_lines or line_vertical_left_up in simulated_lines) and (line_vertical_right_up in used_lines or line_vertical_right_up in simulated_lines) and (line_horizontal_up not in used_lines and line_horizontal_up not in simulated_lines): 
                simulated_lines.append(line_horizontal_up)
                chained_lines.append(line_horizontal_up)
                current_chain_length += 1
                print("8")
                self.chaining(line_horizontal_up, visited_lines, used_lines, simulated_lines)  
            elif (line_horizontal_down in used_lines or line_horizontal_down in simulated_lines) and (line_vertical_left_down in used_lines or line_vertical_left_down in simulated_lines) and (line_vertical_right_down not in used_lines and line_vertical_right_down not in simulated_lines):
                simulated_lines.append(line_vertical_right_down)
                chained_lines.append(line_vertical_right_down)
                current_chain_length += 1
                print("9")
                self.chaining(line_vertical_right_down, visited_lines, used_lines, simulated_lines) 
            elif (line_horizontal_down in used_lines or line_horizontal_down in simulated_lines) and (line_vertical_right_down in used_lines or line_vertical_right_down in simulated_lines) and (line_vertical_left_down not in used_lines and line_vertical_left_down not in simulated_lines):
                simulated_lines.append(line_vertical_left_down)
                chained_lines.append(line_vertical_left_down)
                current_chain_length += 1
                print("10")
                self.chaining(line_vertical_left_down, visited_lines, used_lines, simulated_lines) 
            elif (line_vertical_left_down in used_lines or line_vertical_left_down in simulated_lines) and (line_vertical_right_down in used_lines or line_vertical_right_down in simulated_lines) and (line_horizontal_down not in used_lines and line_horizontal_down not in simulated_lines):
                simulated_lines.append(line_horizontal_down)
                chained_lines.append(line_horizontal_down)
                current_chain_length += 1
                print("11")
                self.chaining(line_horizontal_down, visited_lines, used_lines, simulated_lines) 
                
            print("current_chain_length:" +str(current_chain_length))
                
    def explore_neighbors(self,line,visited_lines, used_lines, simulated_lines, twee_buren_geadd):
        global current_chain_length
        global twee_buren_geadd2

        r, c, o = line
        line_horizontal_left_up = None
        line_horizontal_left_down = None
        line_horizontal_right_up = None
        line_horizontal_right_down = None
        line_vertical_up = None
        line_vertical_down = None
        line_horizontal_left = None
        line_horizontal_right = None
        line_vertical_left_up = None
        line_vertical_left_down = None
        line_vertical_right_up = None
        line_vertical_right_down = None
        line_vertical_right = None
        line_vertical_left = None
        line_horizontal_up = None
        line_horizontal_down = None

        if o == "v":
            line_horizontal_left_up = r, c-1, "h"
            line_horizontal_left_down = r+1, c-1, "h"
            line_horizontal_right_up = r, c, "h"
            line_horizontal_right_down = r+1, c, "h"
            line_vertical_up = r-1, c, "v"
            line_vertical_down = r+1, c, "v"
            line_vertical_left = r, c-1, "v"
            line_vertical_right = r, c+1, "v"
                
        elif o == "h":
            line_horizontal_left = r, c-1, o
            line_horizontal_right = r, c+1, o
            line_vertical_left_up = r-1, c, "v"
            line_vertical_left_down = r, c, "v"
            line_vertical_right_up = r-1, c+1, "v"
            line_vertical_right_down = r, c+1, "v"
            line_horizontal_up = r-1, c, "h"
            line_horizontal_down = r+1, c, "h"
                
        if o == "v":
            if (line_vertical_right in used_lines or line_vertical_right in simulated_lines) and (line_horizontal_right_up not in used_lines and line_horizontal_right_up not in simulated_lines) and (line_horizontal_right_down not in used_lines and line_horizontal_right_down not in simulated_lines):
                self.set_twee_buren()
                simulated_lines.append(line_horizontal_right_up)
                self.look_4_chains(line_horizontal_right_up,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                simulated_lines.append(line_horizontal_right_down)
                self.look_4_chains(line_horizontal_right_down,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                current_chain_length += 1
                twee_buren_geadd = 1
                print("TWEE BLUREN: "+str(twee_buren_geadd))

            
            elif (line_horizontal_right_up in used_lines or line_horizontal_right_up in simulated_lines) and (line_vertical_right not in used_lines and line_vertical_right not in simulated_lines) and (line_horizontal_right_down not in used_lines and line_horizontal_right_down not in simulated_lines):
                self.set_twee_buren()
                simulated_lines.append(line_vertical_right)
                self.look_4_chains(line_vertical_right,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                simulated_lines.append(line_horizontal_right_down)
                self.look_4_chains(line_horizontal_right_down,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                current_chain_length += 1
                twee_buren_geadd = 1
                print("TWEE BLUREN: "+str(twee_buren_geadd))

            elif (line_horizontal_right_down in used_lines or line_horizontal_right_down in simulated_lines) and (line_vertical_right not in used_lines and line_vertical_right not in simulated_lines) and (line_horizontal_right_up not in used_lines and line_horizontal_right_up not in simulated_lines):
                self.set_twee_buren()
                simulated_lines.append(line_vertical_right)
                self.look_4_chains(line_vertical_right,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                simulated_lines.append(line_horizontal_right_up)
                self.look_4_chains(line_horizontal_right_up,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                current_chain_length += 1
                twee_buren_geadd = 1
                print("TWEE BLUREN: "+str(twee_buren_geadd))

            elif (line_vertical_left in used_lines or line_vertical_left in simulated_lines) and (line_horizontal_left_up not in used_lines and line_horizontal_left_up not in simulated_lines) and (line_horizontal_left_down not in used_lines and line_horizontal_left_down not in simulated_lines):
                self.set_twee_buren()
                simulated_lines.append(line_horizontal_left_up)
                self.look_4_chains(line_horizontal_left_up,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                simulated_lines.append(line_horizontal_left_down)
                self.look_4_chains(line_horizontal_left_down,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                current_chain_length += 1
                twee_buren_geadd = 1
                print("TWEE BLUREN: "+str(twee_buren_geadd))

            elif (line_horizontal_left_up in used_lines or line_horizontal_left_up in simulated_lines) and (line_vertical_left not in used_lines and line_vertical_left not in simulated_lines) and (line_horizontal_left_down not in used_lines and line_horizontal_left_down not in simulated_lines):
                self.set_twee_buren()
                simulated_lines.append(line_vertical_left)
                self.look_4_chains(line_vertical_left,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                simulated_lines.append(line_horizontal_left_down)
                self.look_4_chains(line_horizontal_left_down,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                current_chain_length += 1
                twee_buren_geadd = 1
                print("TWEE BLUREN: "+str(twee_buren_geadd))

            elif (line_horizontal_left_down in used_lines or line_horizontal_left_down in simulated_lines) and (line_horizontal_left_up not in used_lines and line_horizontal_left_up not in simulated_lines) and (line_vertical_left not in used_lines and line_vertical_left not in simulated_lines):
                self.set_twee_buren()
                simulated_lines.append(line_horizontal_left_up)
                self.look_4_chains(line_horizontal_left_up,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                simulated_lines.append(line_vertical_left)
                self.look_4_chains(line_vertical_left,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                current_chain_length += 1
                twee_buren_geadd = 1
                print("TWEE BLUREN: "+str(twee_buren_geadd))
                
        if o == "h":
            if (line_horizontal_up  in used_lines or line_horizontal_up  in simulated_lines) and (line_vertical_right_up  not in used_lines and line_vertical_right_up  not in simulated_lines) and (line_vertical_left_up  not in used_lines and line_vertical_left_up  not in simulated_lines):
                self.set_twee_buren()
                simulated_lines.append(line_vertical_right_up)
                self.look_4_chains(line_vertical_right_up,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                simulated_lines.append(line_vertical_left_up)
                self.look_4_chains(line_vertical_left_up,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                current_chain_length += 1
                twee_buren_geadd = 1
                print("TWEE BLUREN: "+str(twee_buren_geadd))

            
            elif (line_vertical_left_up  in used_lines or line_vertical_left_up  in simulated_lines) and (line_horizontal_up  not in used_lines and line_horizontal_up  not in simulated_lines) and (line_vertical_right_up  not in used_lines and line_vertical_right_up  not in simulated_lines):
                self.set_twee_buren()
                simulated_lines.append(line_horizontal_up )
                self.look_4_chains(line_horizontal_up ,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                simulated_lines.append(line_vertical_right_up )
                self.look_4_chains(line_vertical_right_up ,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                current_chain_length += 1
                twee_buren_geadd = 1
                print("TWEE BLUREN: "+str(twee_buren_geadd))

            elif (line_vertical_right_up in used_lines or line_vertical_right_up in simulated_lines) and (line_vertical_left_up  not in used_lines and line_vertical_left_up  not in simulated_lines) and (line_horizontal_up not in used_lines and line_horizontal_up not in simulated_lines):
                self.set_twee_buren()
                simulated_lines.append(line_vertical_left_up )
                self.look_4_chains(line_vertical_left_up ,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                simulated_lines.append(line_horizontal_up)
                self.look_4_chains(line_horizontal_up,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                current_chain_length += 1
                twee_buren_geadd = 1
                print("TWEE BLUREN: "+str(twee_buren_geadd))
                """ --------------------------------------------"""

            elif (line_horizontal_down in used_lines or line_horizontal_down in simulated_lines) and (line_vertical_left_down  not in used_lines and line_vertical_left_down  not in simulated_lines) and (line_vertical_right_down  not in used_lines and line_vertical_right_down  not in simulated_lines):
                self.set_twee_buren()
                simulated_lines.append(line_vertical_left_down )
                self.look_4_chains(line_vertical_left_down ,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                simulated_lines.append(line_vertical_right_down )
                self.look_4_chains(line_vertical_right_down ,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                current_chain_length += 1
                twee_buren_geadd = 1
                print("TWEE BLUREN: "+str(twee_buren_geadd))

            elif (line_vertical_right_down in used_lines or line_vertical_right_down in simulated_lines) and (line_vertical_left_down  not in used_lines and line_vertical_left_down  not in simulated_lines) and (line_horizontal_down  not in used_lines and line_horizontal_down not in simulated_lines):
                self.set_twee_buren()
                simulated_lines.append(line_vertical_left_down )
                self.look_4_chains(line_vertical_left_down ,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                simulated_lines.append(line_horizontal_down  )
                self.look_4_chains(line_horizontal_down  ,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                current_chain_length += 1
                twee_buren_geadd = 1
                print("TWEE BLUREN: "+str(twee_buren_geadd))

            elif (line_vertical_left_down in used_lines or line_vertical_left_down in simulated_lines) and (line_vertical_right_down not in used_lines and line_vertical_right_down not in simulated_lines) and (line_horizontal_down not in used_lines and line_horizontal_down not in simulated_lines):
                self.set_twee_buren()
                simulated_lines.append(line_horizontal_down)
                self.look_4_chains(line_horizontal_down ,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                simulated_lines.append(line_vertical_left_down)
                self.look_4_chains(line_vertical_left_down,visited_lines,used_lines,simulated_lines,twee_buren_geadd)
                current_chain_length += 1
                twee_buren_geadd = 1
                print("TWEE BLUREN: "+str(twee_buren_geadd))
            else:
                print("No need to add 2 neighbors.")
                

        
        
    def look_4_chains(self,line, visited_lines,used_lines,simulated_lines,twee_buren_geadd):
        global current_chain_length
        global twee_buren_geadd2
        print("Look_4_chains: "+str(line))
        r, c, o = line
        line_horizontal_left_up = None
        line_horizontal_left_down = None
        line_horizontal_right_up = None
        line_horizontal_right_down = None
        line_vertical_up = None
        line_vertical_down = None
        line_horizontal_left = None
        line_horizontal_right = None
        line_vertical_left_up = None
        line_vertical_left_down = None
        line_vertical_right_up = None
        line_vertical_right_down = None
        line_vertical_right = None
        line_vertical_left = None
        line_horizontal_up = None
        line_horizontal_down = None

        if o == "v":
            line_horizontal_left_up = r, c-1, "h"
            line_horizontal_left_down = r+1, c-1, "h"
            line_horizontal_right_up = r, c, "h"
            line_horizontal_right_down = r+1, c, "h"
            line_vertical_up = r-1, c, "v"
            line_vertical_down = r+1, c, "v"
            line_vertical_left = r, c-1, "v"
            line_vertical_right = r, c+1, "v"
                
        elif o == "h":
            line_horizontal_left = r, c-1, o
            line_horizontal_right = r, c+1, o
            line_vertical_left_up = r-1, c, "v"
            line_vertical_left_down = r, c, "v"
            line_vertical_right_up = r-1, c+1, "v"
            line_vertical_right_down = r, c+1, "v"
            line_horizontal_up = r-1, c, "h"
            line_horizontal_down = r+1, c, "h"
            

        if line not in visited_lines:
            if (self.return_twee_buren() == 0):
                print("Twee buren is 0 en exploren 2 neighbors")
                self.print_twee_buren()
                self.explore_neighbors(line,visited_lines, used_lines,simulated_lines, twee_buren_geadd)
            else:    
                self.chaining(line, visited_lines, used_lines, simulated_lines)
            visited_lines.append(line)

        elif line not in visited_lines and line in simulated_lines:
            print("toch chaine yeeah")
            self.chaining(line, visited_lines, used_lines, simulated_lines)

        else:
            print ("In visited lines")            
            
            
    
    def return_chains(self,twee_buren_geadd):
        global current_chain_length
        global chain_count
        global twee_buren_geadd2

        visited_lines = []
        simulated_lines = []
        self.reset_chain_counter()
        used_lines = self.used_lines()
        chain_count = 0
        print("")
        print("----------------------------CHAIN ANALYSIS----------------------------")

        for line in used_lines:
            print('\n')
            print('NEW FOR LOOP')

            print("line: "+str(line))
            print("Nazicht twee_buren_geadd2 begin: "+str(self.print_twee_buren()))
            current_chain_length = 1
            self.reset_twee_buren()
            
            self.look_4_chains(line, visited_lines,used_lines, simulated_lines,twee_buren_geadd)
            if current_chain_length >= 3:    
                self.chain_counter()
                print("EUREKA chain ++")
                self.print_count()

            print("Nazicht twee_buren_geadd2 eind: "+str(self.print_twee_buren()))
            print("USED_LINES: "+str(used_lines))
            print("VISITED_LINES: "+str(visited_lines))
            print("SIMULATED_LINES: "+str(simulated_lines))
            print("CHAIN_COUNT: "+str(chain_count))
            print('\n')

        print("----------------------------end----------------------------")
        self.print_count()        
        print("\n")
        
    def count_chains_v2(self):
        twee_buren_geadd = 0
        global chain_count
        self.return_chains(twee_buren_geadd)        
        
        
        
        
        
        
        
        
        
        
        
        
        