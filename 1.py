with open("file1.txt", 'w') as f_obj:
    while True:
        row = input('Введите строку - ')
        if row == '':
            f_obj.close()
            print('Файл сохранён')
            break
        else:
            f_obj.write(row + '\n')
