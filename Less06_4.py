class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        print(f"Новая машина: {self.name} (Цвет {self.color}) машина полицейская - {self.is_police} ")

    def go(self):
        return f'{self.name} Машина Поехала!'

    def stop(self):
        return f'\n{self.name} Машина Остановилась!'

    def turn(self, direction):
        return f'\nМашина {self.name} повернула {direction}'

    def show_speed(self):
        return f'\nСкорость Автомобиля - {self.speed}'


class TownCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость Автомобиля - {self.speed} - Превышение сорости!!!' \
            if self.speed > 60 else f'{self.name}: Скорость Автомобиля - {self.speed}'


class SportCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость Автомобиля - {self.speed} - Превышение сорости!!!' \
            if self.speed > 80 else f'{self.name}: Скорость Автомобиля - {self.speed}'

class WorkCar(Car):
    def show_speed(self):
        return f'{self.name}: Скорость Автомобиля - {self.speed} - Превышение сорости!!!' \
            if self.speed > 40 else f'{self.name}: Скорость Автомобиля - {self.speed}'


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


town = TownCar('Audi', 70, 'blue', False)
print(town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('Lotus', 170, 'red', False)
print(sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('ZAZ', 30, 'red', False)
print(work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar('Dodge', 100, 'yellow', True)
print(police.go(), police.show_speed(), police.turn('right'), police.stop())
