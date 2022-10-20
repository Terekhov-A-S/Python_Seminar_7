import time


class TrafficLight():
    red_color_wait = 7
    yellow_color_wait = 2
    green_color_wait = 5

    red_color_name = 'красный'
    yellow_color_name = 'желтый'
    green_color_name = 'зеленый'

    def __init__(self, color):
        self.__color = color
        print(f'\nОбъект "TrafficLight" со стартовым цветом "{self.__color}" инициирован')

    def lighting_swith(self, color, wait_period):
        self.wait_period = wait_period
        print(f'Включен  свет - {color} (время ожидания: {self.wait_period} сек)')
        time.sleep(self.wait_period)

    def running(self, color=''):
        if not color:
            loc_color = self.__color
        else:
            loc_color = color

        if loc_color == self.red_color_name:
            self.lighting_swith('красный', self.red_color_wait)
            self.lighting_swith('желтый', self.yellow_color_wait)
            self.lighting_swith('зеленый', self.green_color_wait)
        elif loc_color == self.yellow_color_name:
            self.lighting_swith('желтый', self.yellow_color_wait)
            self.lighting_swith('зеленый', self.green_color_wait)
        else:
            self.lighting_swith('зеленый', self.green_color_wait)

        print('Цикл переключения цветов завершен')


tl1 = TrafficLight('красный')
tl1.running()

tl2 = TrafficLight('желтый')
tl2.running()

tl3 = TrafficLight('зеленый')
tl3.running()
