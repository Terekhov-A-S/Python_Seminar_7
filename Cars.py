class Car:

    def __init__(self, color: str, name: str, is_police: bool = False):
        self.color = color
        self.name = name
        self.is_police = True if is_police else False
        self.speed = 0
        self._direction = ''

    def go(self, speed: float):
        try:
            self.speed = float(speed)
        except ValueError:
            pass

    def stop(self):
        self.speed = 0

    def turn(self, direction: str):
        if direction not in ('налево', 'направо'):
            print(f"'{direction}' ошибка направления")
            return
        if not self.speed:
            print(f"Невозможно повернуть {direction} на месте")
            return
        self._direction = direction

    def show_speed(self):
        print(f'Моя скорость: {self.speed} км/ч')

    @property
    def direction(self):
        return self._direction


class TownCar(Car):
    _max_granted_speed = 60

    def __init__(self, *args):
        super().__init__(*args)

    def show_speed(self):
        super().show_speed()
        if self.speed > self._max_granted_speed:
            print('Внимание! Превышение скорости!')


class SportCar(Car):

    def __init__(self, *args):
        super().__init__(*args)


class WorkCar(Car):
    _max_granted_speed = 40

    def __init__(self, *args):
        super().__init__(*args)

    def show_speed(self):
        super().show_speed()
        if self.speed > self._max_granted_speed:
            print('Внимание! Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args, is_police=True)


if __name__ == '__main__':
    cars_data = {
        ('Золотой', 'Aurus Senat Limousine'): TownCar,
        ('Перламутровый', 'Ford Mustang'): SportCar,
        ('Красный', 'Porshe Panamera'): WorkCar,
        ('Белый', 'Dodge Charger Pursuit'): PoliceCar,
    }

    for car_descr, car_cls in cars_data.items():
        car = car_cls(*car_descr)

        print('*-_-*-_-*-_-*-_-*-_-*-_-*-_-*-_-*-_-*-_-*-_-*-_-*-_-*-_-*-_-')
        print(f"Название автомобиля: '{car.name}'")
        print(f"Цвет автомобиля: '{car.color}'")
        print(f"Булево: '{car.is_police}'")
        print(f"Скорость автомобиля: '{car.speed}'")
        print(f"Направление движения автомобиля: '{car.direction}'")
        print(f"Показать скорость автомобиля: '{car.show_speed()}'")

        car.turn('Внимание!')
        car.turn('налево')
        car.go('Внимание!')
        print("Скорость автомобиля после начала движения:", car.speed)
        car.go(30)
        car.show_speed()
        car.go(45)
        car.show_speed()
        car.go(75)
        car.show_speed()
        car.turn('налево')
        print(f"Направление движения автомобиля: '{car.direction}'")
        car.turn('направо')
        print(f"Направление движения автомобиля: '{car.direction}'")
        car.stop()
        car.show_speed()
        print('*-_-*-_-*-_-*-_-*-_-*-_-*-_-*-_-*-_-*-_-*-_-*-_-*-_-*-_-*-_-\n\n')
