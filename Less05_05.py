def summary():
    try:
        with open('5.txt', 'w+') as f:
            line = input('Введите цифры через пробел \n')
            f.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка ввода-вывода')


summary()