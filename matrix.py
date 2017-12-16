class Matrix:
    def __init__(self, rows, columns):
        self.data = [[0 for x in range(columns)] for x in range(rows)]

    def print_matrix(self):
        for i in range(len(self.data)):
            print (self.data[i])

    def set_value(self, row, col, value):
        self.data[row][col] = value

    def as_list(self):
        res = []
        for i in range(len(self.data)):
            res += self.data[i]
        return res


    def reset(self):
        rows = len(self.data)
        columns = len(self.data[0])
        self.data = [[0 for x in range(columns)] for x in range(rows)]
