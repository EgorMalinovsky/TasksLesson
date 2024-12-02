"""
Task_2
Реализовать программу с функционалом калькулятора для операций над двумя числами.
Числа и операция вводятся пользователем с клавиатуры.
Использовать обработку исключений.
"""


def add(x, y):
    """Сложение"""
    return x + y


def subtract(x, y):
    """Вычитание"""
    return x - y


def multiply(x, y):
    """Умножение"""
    return x * y


def divide(x, y):
    """Деление"""
    if y == 0:
        raise ValueError("Ошибка: Деление на ноль невозможно!")
    return x / y


def main():
    print("Калькулятор: ")
    print("Доступные операции: ")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")

    try:
        # Ввод чисел и операции
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        operation = input("Введите операцию (+, -, *, /): ").strip()

        # Выполнение выбранной операции
        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        else:
            raise ValueError("Неверная операция. Пожалуйста, выберите одну из: +, -, *, /")

        # Вывод результата вычисление
        print(f"Результат: {result}")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
