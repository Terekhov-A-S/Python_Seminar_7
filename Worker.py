class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


stanislav = Position('Станислав', 'Стрельбицкий', 'IT-разработчик', 155000, 38000)
print(stanislav.get_full_name())
print(stanislav.position)
print(stanislav.get_total_income())
