class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        self._is_going = False

    def go(self):
        self._is_going = True
        print('машина поехала')

    def stop(self):
        self._is_going = False
        print('машина остановилась')

    def turn(self, direction):
        if self._is_going:
            print('машина повернула' + direction)
        else:
            print('машина не может повернуть - она стоит')

    def show_speed(self):
        if self._is_going:
            print(f'Текущая скорость: {self.speed} км/ч')
        else:
            print(f'Текущая скорость: 0 км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.max_speed = 60

    def show_speed(self):
        super(TownCar, self).show_speed()
        if self._is_going and self.speed > self.max_speed:
            print('превышение скорости')


class WorkCar(TownCar):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.max_speed = 40


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


class SportCar(Car):
    pass


car_1 = TownCar(60, 'синий', 'запорожец')
print(car_1.__dict__.items())
car_1.show_speed()
car_1.go()
car_1.show_speed()

car_2 = WorkCar(50, 'красный', 'спиртовоз')
print(car_2.__dict__.items())
car_2.show_speed()
car_2.go()
car_2.show_speed()

car_3 = PoliceCar(100, 'чёрный', 'воронок')
print(car_3.__dict__.items())
