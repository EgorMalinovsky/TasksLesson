"""
Task_2
Дан список чисел. С помощью filter() получить список
тех элементов из исходного списка, значение которых
больше 0.
"""

# Ввод списка чисел
numbers = list(map(int, input("Введите числа, разделённые пробелом: ").split()))

# Фильтр на числа больше 0
positive_numbers = list(filter(lambda x: x > 0, numbers))

# Вывод результата
print(positive_numbers)
