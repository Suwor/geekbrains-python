class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


position = Position('Иванов', 'Иван', 'подниматель пингвинов', {"wage": 100, "bonus": 50})
print(position.get_full_name(), position.get_total_income(), position.__dict__.items())
