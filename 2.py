all_rows = 0
with open("file2.txt") as f_obj:
    for line in f_obj:
        print(f'Строка {all_rows+1}, кол-во слов {len(line.split())}')
        all_rows += 1
print(f'Всего строк: {all_rows}')
