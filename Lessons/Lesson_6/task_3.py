"""
Task_3
Программа получает на вход число.
Реализовать функцию, которая определяет, является ли это число простым
(делится только на единицу и на само себя).
"""

# Ввод пользователем числа
number_input = int(input(f"Введите число для проверки является ли оно простым: "))


# Функция на проверку того, является ли число простым
def checking_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, number // 2+1):
        if number % i == 0:
            return False
    return True


if checking_prime_number(number_input):
    print(f"Число {number_input} не является простым")
else:
    print(f"Число {number_input} является простым")
