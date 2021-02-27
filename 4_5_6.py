class Store:
    def __init__(self):
        self.store_list = []

    def add_item(self):
        division, item_type, count = input('Введите через пробел: подразделение, тип техники, количество - ').split()
        if not count.isdigit():
            print('Количество указано неверно')
            return
        if item_type.upper() == OfficeEquipment.printer_name:
            self.store_list.append([Printer(int(input('Введите количество краски - '))), division, count])
        elif item_type.upper() == OfficeEquipment.scanner_name:
            self.store_list.append([Scanner(int(input('Введите количество бумаги - '))), division, count])
        elif item_type.upper() == OfficeEquipment.copier_name:
            self.store_list.append([
                Copier(int(input('Введите количество краски - ')), int(input('Введите количество бумаги - '))),
                division,
                count
            ])
        else:
            print('Тип техники указан неверно')
            return
        print('Товар добавлен')
        print()


class OfficeEquipment:
    printer_name = 'ПРИНТЕР'
    scanner_name = 'СКАНЕР'
    copier_name = 'КСЕРОКС'

    def __init__(self, equipment_name):
        self.equipment_name = equipment_name


class Printer(OfficeEquipment):
    def __init__(self, paint_amount):
        super().__init__(OfficeEquipment.printer_name)
        self.paint_amount = paint_amount


class Scanner(OfficeEquipment):
    def __init__(self, paper_amount):
        super().__init__(OfficeEquipment.scanner_name)
        self.paper_amount = paper_amount


class Copier(Printer, Scanner):
    def __init__(self, paint_amount, paper_amount):
        super().__init__(OfficeEquipment.copier_name)
        self.paint_amount = paint_amount
        self.paper_amount = paper_amount


my_store = Store()

print(not "5".isdigit())


while True:
    el = input('Введите + для добавления товара или "Enter" для выхода - ')
    if el == '+':
        my_store.add_item()
    else:
        print(my_store.store_list)
        break
