class ListElementError(Exception):
    def __init__(self, txt):
        self.txt = txt


def list_append(my_list, element):
    if element.isdigit():
        my_list.append(int(element))
    else:
        raise ListElementError('Нужно вводить только числа')


nums = []
while True:
    el = input('Введите число или Q для выхода - ')
    if el.upper() == 'Q':
        break
    else:
        try:
            list_append(nums, el)
        except:
            print('Нужно вводить только числа')

print(nums)
