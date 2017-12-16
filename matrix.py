class Matrix:
    def __init__(self, rows, columns):
        self.data = [[0 for x in range(columns)] for x in range(rows)]

    def print_matrix(self):
        for i in range(len(self.data)):
            print (self.data[i])

    def set_value(self, row, col, value):
        self.data[row][col] = value
