"""
Task_7
Реализовать функцию,
которая создаёт матрицу размером M строк на N столбцов и заполняет её рандомными числами.
"""

import random

# Пример использования


def create_random_matrix(m, n, min_value=0, max_value=100):
    return [[random.randint(min_value, max_value) for _ in range(n)] for _ in range(m)]


# Ввод данных
rows = int(input("Введите количество строк (M): "))
cols = int(input("Введите количество столбцов (N): "))
min_val = int(input("Введите минимальное значение: "))
max_val = int(input("Введите максимальное значение: "))

# Создание матрицы
matrix = create_random_matrix(rows, cols, min_val, max_val)

# Вывод результата
print("Сгенерированная матрица:")
for row in matrix:
    print(row)
