class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def goto(self, new_floor: int):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f"В этом доме нет этажа {new_floor}")
        else:
            [print(i) for i in range(1, new_floor + 1)]


lastochka = House("ЖК Ласточка", 5)

lastochka.goto(5)
lastochka.goto(10)
lastochka.goto(4)
lastochka.goto(0)
