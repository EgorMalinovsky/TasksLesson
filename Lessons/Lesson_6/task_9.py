"""
Task_9
Реализовать функцию,
которая находит суммуэлементов матрицы (матрица M x N).
Определить, какую долю в общей сумме (процент) составляет сумма элементов каждого столбца.
"""

import random


def matrix_column_percentage(matrix):
    # Словарь для нахождения суммы элементов матрицы и процент суммы элементов каждого столбца от общей суммы
    total_sum = sum(sum(row) for row in matrix)
    columns_sum = [sum(matrix[row][col] for row in range(len(matrix))) for col in range(len(matrix[0]))]
    columns_percentage = [(col_sum / total_sum) * 100 for col_sum in columns_sum]
    return columns_percentage, total_sum


# Ввод пользователем значений и генерация матрицы
def main():
    rows = int(input("Введите количество строк (M): "))
    cols = int(input("Введите количество столбцов (N): "))
    min_val = int(input("Введите минимальное значение для генерации матрицы: "))
    max_val = int(input("Введите максимальное значение для генерации матрицы: "))
    matrix = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

    # Вывод сгенерированной матрицы
    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)

    # Вычисление процентов и общей суммы
    column_percentages, total_sum = matrix_column_percentage(matrix)

    # Вывод результата
    print(f"Общая сумма всех элементов матрицы: {total_sum}")
    for i, percentage in enumerate(column_percentages):
        print(f"Процент суммы элементов столбца {i + 1}: {percentage:.2f}%")


if __name__ == "__main__":
    main()
