"""
Task_8
Реализовать функцию,
которая находит минимальный и максимальный элементы в матрице (матрица M x N).
Вывестив консоль индексы найденных элементов.
"""


import random


# Словарь для нахождения мин и макс элемента и их индексов
def find_min_max_in_matrix(matrix):
    min_val = float('inf')
    max_val = float('-inf')
    min_index = (-1, -1)
    max_index = (-1, -1)

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value < min_val:
                min_val = value
                min_index = (i, j)
            if value > max_val:
                max_val = value
                max_index = (i, j)

    return {
        "min_value": min_val,
        "min_index": min_index,
        "max_value": max_val,
        "max_index": max_index,
    }

# Ввод пользователем значений и генерация матрицы


def main():
    rows = int(input("Введите количество строк (M): "))
    cols = int(input("Введите количество столбцов (N): "))
    min_val = int(input("Введите минимальное значение для генерации матрицы: "))
    max_val = int(input("Введите максимальное значение для генерации матрицы: "))

    matrix = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)

    # Нахождение минимального и максимального элементов
    result = find_min_max_in_matrix(matrix)

    # Вывод результата
    print(f"Минимальное значение: {result['min_value']} на позиции {result['min_index']}")
    print(f"Максимальное значение: {result['max_value']} на позиции {result['max_index']}")


if __name__ == "__main__":
    main()

