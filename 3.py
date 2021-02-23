class Cell:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        result = self.amount - other.amount
        if result > 0:
            return Cell(result)
        else:
            raise ArithmeticError('Количество ячеек не может быть меньше нуля')

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __truediv__(self, other):
        return Cell(self.amount // other.amount)

    def make_order(self, length):
        for i in range(self.amount):
            if i % length == 0:
                print('\n', end='')
            print('*', end='')


cell_1 = Cell(10)
cell_2 = Cell(15)
cell_3 = cell_1 + cell_2
print(cell_3.amount)

cell_1 = Cell(20)
cell_2 = Cell(15)
cell_3 = cell_1 - cell_2
print(cell_3.amount)

cell_1 = Cell(20)
cell_2 = Cell(15)
cell_3 = cell_1 * cell_2
print(cell_3.amount)

cell_1 = Cell(20)
cell_2 = Cell(2)
cell_3 = cell_1 / cell_2
print(cell_3.amount)

cell_1 = Cell(47)
cell_1.make_order(20)
