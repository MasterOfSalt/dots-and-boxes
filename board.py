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
        for ri in range(len(self.cells)):
            row = self.cells[ri]
            for ci in range(len(row)):
                cell = row[ci]
                if ri < (len(self.cells) - 1) and cell["v"] == 0:
                    free_lines.append((ri, ci, "v"))
                if ci < (len(row) - 1) and cell["h"] == 0:
                    free_lines.append((ri, ci, "h"))
        return free_lines
