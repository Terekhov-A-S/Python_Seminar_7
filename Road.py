class Road:
    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def get_mass(self, square_meter: int, coating_thickness: int) -> int:
        mass = self._length * self._width * square_meter * coating_thickness // 100
        return mass


square_meter = int(input('Введите массу асфальта для покрытия 1 кв. метра (в кв. метрах) '))
coating_thickness = int(input('Введите толщину покрытия (в метрах) '))
road = Road(5000, 20)

print(f'Масса в кг: {road.get_mass(square_meter, coating_thickness)}'
      f', масса в тоннах: {road.get_mass(square_meter, coating_thickness) // 1000}')
