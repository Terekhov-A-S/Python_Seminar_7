class Worker:

    def __init__(self, name: str, surname: str, position: str, wage: float = 0, bonus: float = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self, reverse=False):
        return ' '.join(sorted([self.name, self.surname], reverse=reverse))

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    position_data = [
        {'name': 'Станислав', 'surname': 'Стрельбицкий', 'position': 'IT-разработчик', 'wage': 155000, 'bonus': 38000},
        {'name': 'Николай', 'surname': 'Колесников', 'position': 'военнослужащий', 'wage': 67000, 'bonus': 30000},
        {'name': 'Виктория', 'surname': 'Боженко', 'position': 'секретарь', 'wage': 80000, 'bonus': 25000},
    ]

    for item in position_data:
        position = Position(**item)

        print('*_-_*_-_*_-_*_-_*_-_*_-_*_-_*_-_*_-_*_-_*_-_*_-_*_-_*_-_*_-_')
        print('Имя: ', position.name)
        print('Фамилия: ', position.surname)
        # print('Фамилия, имя: ', position.get_full_name())
        # print('Имя, фамилия: ', position.get_full_name(reverse=True))
        print('Должность: ', position.position)
        print('Заработная плата (оклад+премия, тыс. руб.): ', position.get_total_income())
        print('*_-_*_-_*_-_*_-_*_-_*_-_*_-_*_-_*_-_*_-_*_-_*_-_*_-_*_-_*_-_\n\n')
