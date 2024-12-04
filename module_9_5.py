from random import choice

# Пользовательский класс исключения StepValueError
class StepValueError(ValueError):
    """Исключение для недопустимого значения шага."""
    pass

# Класс итератора
class Iterator:
    def __init__(self, start, stop, step=1):
        """
        Инициализация итератора.
        :param start: начальное значение.
        :param stop: конечное значение.
        :param step: шаг итерации.
        """
        if step == 0:
            raise StepValueError("Шаг не может быть равен 0")
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        """Сбрасывает pointer на start и возвращает сам итератор."""
        self.pointer = self.start
        return self

    def __next__(self):
        """
        Увеличивает pointer на step и возвращает текущее значение.
        Завершает итерацию, если pointer выходит за пределы stop.
        """
        if (self.step > 0 and self.pointer >= self.stop) or (self.step < 0 and self.pointer <= self.stop):
            raise StopIteration
        current = self.pointer
        self.pointer += self.step
        return current

# Пример использования
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=" ")
except StepValueError:
    print("Шаг указан неверно")

iter2 = Iterator(-5, 2)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=" ")
print()

for i in iter3:
    print(i, end=" ")
print()

for i in iter4:
    print(i, end=" ")
print()

for i in iter5:
    print(i, end=" ")
print()

