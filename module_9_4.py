from random import choice

# Lambda-функция для сравнения букв в той же позиции
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)

# Замыкание для записи данных в файл
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as f:
            for data in data_set:
                f.write(str(data) + '\n')
    return write_everything

# Использование замыкания
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
# Данные записаны в файл 'example.txt' в указанном виде.


# Класс MysticBall с методом __call__
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

# Использование класса MysticBall
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())  # Случайный выбор слова
print(first_ball())  # Случайный выбор слова
print(first_ball())  # Случайный выбор слова
