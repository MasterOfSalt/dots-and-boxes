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
