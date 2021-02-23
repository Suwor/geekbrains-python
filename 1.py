class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        result = ''
        for row in self.matrix_list:
            result += "|"
            for cell in row:
                result += "{:>5} |".format(cell)
            result += "\n"

        return result

    def __add__(self, other):
        for row_index, row in enumerate(self.matrix_list):
            for cell_index, cell in enumerate(row):
                self.matrix_list[row_index][cell_index] = cell + other.matrix_list[row_index][cell_index]
        return self


x = Matrix([[1, 2, 3], [1, 25, 3], [-85, 12, 3]])
y = Matrix([[1, 2, 3], [1, 25, 3], [-85, 12, 3]])
print(x + y)
