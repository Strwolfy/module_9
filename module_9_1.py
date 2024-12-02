def apply_all_func(int_list, *functions):
    # Создаём пустой словарь для хранения результатов
    results = {}
    # Перебираем каждую переданную функцию
    for func in functions:
        # Вызываем функцию с int_list и записываем результат в словарь
        results[func.__name__] = func(int_list)
    return results

# Пример использования
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
