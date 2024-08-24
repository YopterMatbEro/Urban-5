class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def goto(self, new_floor: int):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f"В этом доме нет этажа {new_floor}")
        else:
            [print(i) for i in range(1, new_floor + 1)]

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


if __name__ == '__main__':
    # Данные для первого задания. Вынес, чтобы при импорте не обрабатывались
    lastochka = House("ЖК Ласточка", 5)

    lastochka.goto(5)
    lastochka.goto(10)
    lastochka.goto(4)
    lastochka.goto(0)
