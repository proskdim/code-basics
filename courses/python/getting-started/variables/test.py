# Проверяем наличие переменных
assert 'x' in globals(), "Переменная x не определена"
assert 'y' in globals(), "Переменная y не определена"
assert x == 10, f"x должен быть 10, а не {x}"
assert y == 20, f"y должен быть 20, а не {y}"

# Проверяем функцию
result = sum()
expected = 30
assert result == expected, f"Ожидалось {expected}, получено {result}"

print("OK")
