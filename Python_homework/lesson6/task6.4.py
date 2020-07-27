class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        if self.speed != 0:
                print(f'Автомобиль {self.name} начал движение')
        else:
                print(f'Автомобиль {self.name} пока не начал движение')

    def stop(self):
        if self.speed == 0:
                print(f'Автомобиль {self.name} остановился')
        else:
                print(f'Автомобиль {self.name} пока не остановился и находится в движении')

    def turn (self, direction):
        if direction == 'left' or 'налево':
                print(f'Автомобиль {self.name} повернул налево')
        elif direction == 'right' or 'направо':
                print(f'Автомобиль {self.name} повернул направо')

    def show_speed (self):
        print(f'Скорость автомобиля {self.name} составляет {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} составляет {self.speed} км/ч')
        if self.speed > 60:
            print('Внимание! Скорость превышена!')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} составляет {self.speed} км/ч')
        if self.speed > 40:
            print('Внимание! Скорость превышена!')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

town = TownCar(0, 'Red', 'Lada', False)
town.stop()
work = WorkCar(50, 'Silver', 'Wolkswagen', False)
work.turn('right')
work.show_speed()
sport = SportCar(100, 'White', 'Ferrari', False)
sport.stop()
police = PoliceCar(60, 'Gray', 'UAZ', True)
police.turn('налево')