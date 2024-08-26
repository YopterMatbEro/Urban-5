class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # obj = super().__new__(cls)
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __len__(self):
        if isinstance(self.number_of_floors, int):
            return self.number_of_floors
        else:
            raise TypeError('Кол-во этажей должно быть целым числом')

    def __eq__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other, object):
            return self.number_of_floors == other
        else:
            raise TypeError('Кол-во этажей должно быть целым числом')

    def __ne__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors
        else:
            raise TypeError('Кол-во этажей должно быть целым числом')

    def __lt__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors
        else:
            raise TypeError('Кол-во этажей должно быть целым числом')

    def __le__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors
        else:
            raise TypeError('Кол-во этажей должно быть целым числом')

    def __gt__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors
        else:
            raise TypeError('Кол-во этажей должно быть целым числом')

    def __ge__(self, other):
        if isinstance(self.number_of_floors, int) and isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors
        else:
            raise TypeError('Кол-во этажей должно быть целым числом')

    def __add__(self, value):
        if isinstance(self.number_of_floors, int) and isinstance(value, int):
            self.number_of_floors += value
            return self.number_of_floors
        else:
            raise TypeError('Кол-во этажей должно быть целым числом')

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        if isinstance(self.number_of_floors, int) and isinstance(value, int):
            self.number_of_floors -= value
            return self.number_of_floors
        else:
            raise TypeError('Кол-во этажей должно быть целым числом')

    def __rsub__(self, value):
        return self.__sub__(value)

    def __isub__(self, value):
        return self.__sub__(value)

    def __mul__(self, value):
        if isinstance(self.number_of_floors, int) and isinstance(value, int):
            self.number_of_floors *= value
            return self.number_of_floors
        else:
            raise TypeError('Кол-во этажей должно быть целым числом')

    def __rmul__(self, value):
        return self.__mul__(value)

    def __imul__(self, value):
        return self.__mul__(value)

    def __truediv__(self, value):
        if isinstance(self.number_of_floors, int) and isinstance(value, int):
            self.number_of_floors /= value
            return self.number_of_floors
        else:
            raise TypeError('Кол-во этажей должно быть целым числом')

    def __rtruediv__(self, value):
        return self.__truediv__(value)

    def __itruediv__(self, value):
        return self.__truediv__(value)

    def __floordiv__(self, value):
        if isinstance(self.number_of_floors, int) and isinstance(value, int):
            self.number_of_floors //= value
            return self.number_of_floors
        else:
            raise TypeError('Кол-во этажей должно быть целым числом')

    def __rfloordiv__(self, value):
        return self.__rfloordiv__(value)

    def __ifloordiv__(self, value):
        return self.__rfloordiv__(value)

    def __mod__(self, value):
        if isinstance(self.number_of_floors, int) and isinstance(value, int):
            self.number_of_floors %= value
            return self.number_of_floors
        else:
            raise TypeError('Кол-во этажей должно быть целым числом')

    def __rmod__(self, value):
        return self.__mod__(value)

    def __imod__(self, value):
        return self.__mod__(value)

    def __pow__(self, value):
        if isinstance(self.number_of_floors, int) and isinstance(value, int):
            self.number_of_floors **= value
            return self.number_of_floors
        else:
            raise TypeError('Кол-во этажей должно быть целым числом')

    def __rpow__(self, value):
        return self.__pow__(value)

    def __ipow__(self, value):
        return self.__pow__(value)

    def goto(self, new_floor: int):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f"В этом доме нет этажа {new_floor}")
        else:
            [print(i) for i in range(1, new_floor + 1)]


if __name__ == '__main__':
    # Данные для первого задания. Вынес, чтобы при импорте не обрабатывались
    lastochka = House("ЖК Ласточка", 5)

    lastochka.goto(5)
    lastochka.goto(10)
    lastochka.goto(4)
    lastochka.goto(0)
