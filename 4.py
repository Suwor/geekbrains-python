numerals_en = ['One', 'Two', 'Three', 'Four']
numerals_ru = ['Один', 'Два', 'Три', 'Четыре']
with open("file4.1.txt") as f_obj_r, open("file4.2.txt", 'w') as f_obj_w:
    for line in f_obj_r:
        row_list = line.split()
        row_list.insert(0, numerals_ru[numerals_en.index(row_list.pop(0))])
        f_obj_w.write(' '.join(row_list) + '\n')
