class MyError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        while True:
            try:
                user_val = int(input('Введите числа: '))
                ex = input(f'Всё отлично, добавляем "{user_val}" в список. Хотите продолжить? Y/N: ').upper()
                self.my_list.append(user_val)
                if ex == 'n':
                    print(self.my_list)
                    break

            except ValueError:
                ex = input(f"Вы ввели не число! Хотите продолжить? Y/N: ").upper()
                if ex == 'n':
                    print(self.my_list)
                    break
                else:
                    self.check_value()

a = TypeCheck()
a.check_value()
