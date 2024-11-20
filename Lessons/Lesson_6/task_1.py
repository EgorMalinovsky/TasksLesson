"""
Task_1
Дан список чисел, отсортированных по возрастанию.
На вход принимается значение, равное одному из элементовсписка.
Реализовать функцию, выполняющую рекурсивный алгоритм бинарного поиска,
на выходе программа должна вывести позицию искомого элемента в исходном списке.
"""
# Создаем список для примера
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8]
# Ввод пользователем числа для поиска в спике
value = int(input(f"Введите число для поиска в списке {sorted_list}: "))


def binary_search(arr, target, left, right):
    if left > right:
        return -1

    # Определяем середину списка
    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    # Делим список попалам, выполняя поиск на левую, если введенный элемент меньше, и правую если наоборот
    if target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)

    return binary_search(arr, target, mid + 1, right)


# Функция для нахождения позиции элемента
def find_position(arr, target):
    return binary_search(arr, target, 0, len(arr) - 1)


position = find_position(sorted_list, value)

if position != -1:
    print(f"Введенное число:{value} найдено на позиции {position}")
else:
    print(f"Число {value} не найдено в списке")
