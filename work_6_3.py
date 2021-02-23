class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surmame = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surmame

    def get_total_income(self):
        return f'{sum(self._income.values())}'

p = Position('Alexandr', 'Shulyak', 'Operator', 20000, 5000)
print(f'{p.get_full_name()}\n {p.position}\n {p.get_total_income()}')
