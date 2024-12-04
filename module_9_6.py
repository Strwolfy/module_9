# Функция-генератор all_variants
def all_variants(text):
    """
    Генератор возвращает все подпоследовательности переданной строки text.
    """
    # Проходимся по каждому индексу начала подпоследовательности
    for start in range(len(text)):
        # Проходимся по каждому индексу конца подпоследовательности
        for end in range(start + 1, len(text) + 1):
            # Используем yield для возвращения текущей подпоследовательности
            yield text[start:end]

# Вызов функции-генератора и итерация
a = all_variants("abc")
for i in a:
    print(i)