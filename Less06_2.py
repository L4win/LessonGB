class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Для покрытия всего дорожного полотна неободимо {round(asphalt_mass)} массы асфальта')


Meaning = Road(int(input('Введите Длину: ')), int(input('Введите Ширину: ')))
Meaning.asphalt_mass()