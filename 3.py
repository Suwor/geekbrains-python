from statistics import mean

salary_list = []
with open("file3.txt") as f_obj:
    for line in f_obj:
        row_list = line.split()
        salary = int(row_list[1])
        salary_list.append(salary)
        if salary < 20:
            print(f'У сотрудника {row_list[0]} ЗП = {salary}, что меньше 20')

print(f'Средняя ЗП = {mean(salary_list)}')
