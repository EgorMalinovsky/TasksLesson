"""
Task_14
Дана матрица M x N.
Исходная матрица состоит из нулей и единиц.
Реализовать функцию, которая добавит к матрице ещё один столбец,
элементы которого делает количество единиц в соответствующей строке чётным.
"""

import random


def main():
    # Ввод пользователем значений и генерация матрицы
    rows = int(input("Введите количество строк (M): "))
    cols = int(input("Введите количество столбцов (N): "))

    # Генерация матрицы с 0 и 1
    matrix = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

    print("Исходная матрица:")
    for row in matrix:
        print(row)

    # Добавление столбца
    matrix_with_added_column = add_column_to_make_odd_even(matrix)

    print("\nМатрица после добавления столбца:")
    for row in matrix_with_added_column:
        print(row)


def add_column_to_make_odd_even(matrix):
    # Функция для добавления столбца в матрицу, и делает четным

    for row in matrix:
        # Подсчитываем количество единиц в строке
        ones_count = row.count(1)

        # Если количество единиц нечетное, добавляем 1, иначе 0
        if ones_count % 2 == 0:
            row.append(0)  # Если четное, добавляем 0
        else:
            row.append(1)  # Если нечетное, добавляем 1

    return matrix


if __name__ == "__main__":
    main()
