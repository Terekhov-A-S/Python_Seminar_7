class Stationery:
    title: str

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    title = "Ручка"

    def draw(self):
        print(f"{self.title} - для начертания текста")


class Pencil(Stationery):
    title = "Карандаш"

    def draw(self):
        print(f"{self.title} - для начертания чертежей и рисунков")


class Handle(Stationery):
    title = "Маркер"

    def draw(self):
        print(f"{self.title} - для выделения и начертания полужирного текста")


if __name__ == '__main__':
    stationery = Stationery()
    stationery.draw()
    pen = Pen()
    pen.draw()
    pencil = Pencil()
    pencil.draw()
    handle = Handle()
    handle.draw()
