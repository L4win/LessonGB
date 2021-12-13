with open('3.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Средняя ЗП = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'Сотрудники с ЗП меньше 20т. {[e[0] for e in employees_dict.items() if e[1] < 20000]}')