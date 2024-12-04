# Дано два списка
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для разницы длин строк, если их длины не равны (с использованием zip)
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для сравнения длин строк на одинаковых позициях (без zip)
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Проверка результатов
print(list(first_result))  # Результат: [1, 2]
print(list(second_result))  # Результат: [False, False, True]