"""
Task_13
Реализовать функцию,
которая находит сумму элементов на главной диагонали
и сумму элементов на побочной диагонали (матрица M x N).
"""

import random


def main():
    # Ввод пользователем значений и генерация матрицы
    rows = int(input("Введите количество строк (M): "))
    cols = int(input("Введите количество столбцов (N): "))
    min_val = int(input("Введите минимальное значение для генерации матрицы: "))
    max_val = int(input("Введите максимальное значение для генерации матрицы: "))

    # Генерация матрицы
    matrix = [
        [random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

    # Печать матрицы
    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)

    # Нахождение суммы элементов диагоналей
    result = find_diagonal_sums(matrix)

    # Вывод результата
    print(f"Сумма элементов главной диагонали: {result['main_diag_sum']}")
    print(f"Сумма элементов побочной диагонали: {result['secondary_diag_sum']}")


def find_diagonal_sums(matrix):
    # Функция для определения сумму элементов на главной и побочной диагонали матрицы
    main_diag_sum = 0
    secondary_diag_sum = 0
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(min(rows, cols)):
        main_diag_sum += matrix[i][i]
        secondary_diag_sum += matrix[i][cols - i - 1]

    return {
        "main_diag_sum": main_diag_sum,
        "secondary_diag_sum": secondary_diag_sum,
    }


if __name__ == "__main__":
    main()
