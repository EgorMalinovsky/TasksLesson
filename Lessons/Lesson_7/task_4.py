"""
Task_4
Сделать декоратор, который измеряет время,
затраченное на выполнение декорируемой функции.
"""

import random
import time


# Декоратор для измерения времени выполнения функции в секундах
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        # Отсчет начала времени
        start_time = time.time()
        # Выполняем декорируемую функцию
        result = func(*args, **kwargs)
        # Конец отсчета времени на выполнение функции
        end_time = time.time()
        # Время в секундах
        execution_time_sec = end_time - start_time
        # Вывод времени выполнения функции в секундах
        print(f"Время выполнения функции '{func.__name__}': {execution_time_sec:.6f} секунд")
        return result

    return wrapper


# Главная функция с генерацией матрицы и вычислением сумм диагоналей
@timing_decorator
def main():
    # Ввод пользователем значений и генерация матрицы
    rows = int(input("Введите количество строк (M): "))
    cols = int(input("Введите количество столбцов (N): "))
    min_val = int(input("Введите минимальное значение для генерации матрицы: "))
    max_val = int(input("Введите максимальное значение для генерации матрицы: "))

    # Генерация матрицы
    matrix = [
        [random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)
    ]

    # Вывод созданной матрицы
    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)

    # Нахождение суммы элементов диагоналей
    result = find_diagonal_sums(matrix)

    # Вывод результата
    print(f"Сумма элементов главной диагонали: {result['main_diag_sum']}")
    print(f"Сумма элементов побочной диагонали: {result['secondary_diag_sum']}")


# Функция для вычисления суммы элементов диагоналей
@timing_decorator
def find_diagonal_sums(matrix):
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
