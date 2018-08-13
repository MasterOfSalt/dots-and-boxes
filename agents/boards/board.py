import logging
from timeit import Timer

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
            
            

            
    def chaining(self,line,visited_lines):
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
            line_vertical_left = r, c-1, "v"
            line_vertical_right = r, c+1, "v"
                
            """if line has 1 ontbrekende buur"""
            if line_vertical_right in used_lines and line_horizontal_right_up in used_lines and line_horizontal_right_down not in used_lines:
                used_lines.append(line_horizontal_right_down)
                """visited_lines.append(ALLE QUATRO)???"""
                current_chain_length += 1
                chaining(line_horizontal_right_down)
  
            elif o == "h":
                line_horizontal_left = r, c-1, o
                line_horizontal_right = r, c+1, o
                line_vertical_left_up = r-1, c, "v"
                line_vertical_left_down = r, c, "v"
                line_vertical_right_up = r-1, c+1, "v"
                line_vertical_right_down = r, c+1, "v"
                
                line_horizontal_up = r-1, c, "h"
                line_horizontal_down = r+1, c, "h"
                
    def chaining2(self,line,visited_lines):
        global twee_buren_geadd
        if line_vertical_right in used_lines and line_horizontal_right_up not in used_lines and line_horizontal_right_down not in used_lines:
                used_lines.append(line_horizontal_right_up)
                used_lines.append(line_horizontal_right_down)
                current_chain_length += 1
                twee_buren_geadd = True
                chain_neighbors_v2(self,line_horizontal_right_up,visited_lines)
                chain_neighbors_v2(self,line_horizontal_right_down,visited_lines)
                
        
    def chain_neighbors_v2(self,line, visited_lines,used_lines):
        global current_chain_length
        if line not in visited_lines:

            if twee_buren_geadd is False:
                chaining2(line)
            chaining(line)
            
            visited_lines.append(line)
                
            if line_vertical_right_down in used_lines and line_vertical_right_down not in visited_lines:
                current_chain_length += 1
                self.chain_neighbors(line_vertical_right_down, visited_lines )
                visited_lines.append(line_vertical_right_down)

        else:
            """print ("In visited lines")"""            
            
            
            
    def is_chain_v2(self):
        global current_chain_length
        global chain_count
        visited_lines = []
        self.reset_chain_counter()
        used_lines = self.used_lines()
        print("")
        print("----------------------------CHAIN ANALYSIS----------------------------")
        for line in used_lines:
            current_chain_length = 1
            chain_count = 0
            """print("LINE IS:"+str(line))"""

            self.chain_neighbors_v2(line, visited_lines,used_lines)
            if current_chain_length >= 3:    
                self.chain_counter()
                print("EUREKA chain ++")
                
            """print('\n')
            print("USED_LINES: "+str(used_lines))
            print("VISITED_LINES: "+str(visited_lines))
            print('\n')
            print("NEW Chain count: "+str(self.chain_count))"""
        print("----------------------------end----------------------------")
        self.print_count()

    def chain_counter(self):
        global chain_count
        self.chain_count = self.chain_count+1    
        
    def reset_chain_counter(self):
        global chain_count
        self.chain_count = 0    
        
    def print_count(self):
        global chain_count
        print (self.chain_count) 
        
    def count_chains(self):
        global chain_count
        self.is_chain()
        
                
    def count_chains_v2(self):
        global chain_count_v2
        self.is_chain_v2()
        
        
        
    def fill_line(self,row,column,orientation,player):
        self.cells[row][column][orientation] = player
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        