"""
Task_12
Программа получает на вход число H.
Реализовать функцию, которая определяет, какие столбцы имеют хотя бы одно такое же число,
а какие не имеют (матрица M x N).
"""

import random


def main():
    # Ввод пользователем значений и генерация матрицы
    rows = int(input("Введите количество строк (M): "))
    cols = int(input("Введите количество столбцов (N): "))
    min_val = int(input("Введите минимальное значение для генерации матрицы: "))
    max_val = int(input("Введите максимальное значение для генерации матрицы: "))
    h = int(input("Введите число H для поиска: "))

    # Генерация матрицы
    matrix = [
        [random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)
    ]

    # Печать матрицы
    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)

    # Нахождение столбцов с числом h
    columns_with_h, columns_without_h = find_columns_with_number(matrix, h)

    # Вывод результата
    print(f"Столбцы, содержащие хотя бы одно число {h}: {columns_with_h}")
    print(f"Столбцы, не содержащие число {h}: {columns_without_h}")


def find_columns_with_number(matrix, h):
    # Функция для определения столбцов содержащие хотя бы одно вхождение числа h, а какие не содержат
    columns_with_h = []
    columns_without_h = []

    for col in range(len(matrix[0])):
        found = False
        for row in range(len(matrix)):
            if matrix[row][col] == h:
                found = True
                break
        if found:
            columns_with_h.append(col)
        else:
            columns_without_h.append(col)

    return columns_with_h, columns_without_h


if __name__ == "__main__":
    main()

