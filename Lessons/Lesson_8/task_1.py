"""
Task_1
Реализовать программу для подсчёта индекса массы тела человека.
Пользователь вводит рост и вес с клавиатуры.
На выходе – ИМТ и пояснение к нему в зависимости от попадания в тот или иной диапазон.
Использовать обработку исключений.
"""


def calculate_bmi(weight, height_cm):
    """Функция для расчёта индекса массы тела (ИМТ), где height_cm - рост в сантиметрах"""
    height_m = height_cm / 100  # Переводим рост из сантиметров в метры
    return weight / (height_m ** 2)


def interpret_bmi(bmi):
    """Функция для интерпретации ИМТ"""
    if bmi < 18.5:
        return "Недостаточный вес"
    elif 18.5 <= bmi < 25:
        return "Нормальный вес"
    elif 25 <= bmi < 30:
        return "Избыточный вес"
    else:
        return "Ожирение"


def calculate_weight_for_normal_bmi(height_cm):
    """Функция для вычисления нормального диапазона веса"""
    height_m = height_cm / 100
    min_normal_weight = 18.5 * (height_m ** 2)
    max_normal_weight = 24.9 * (height_m ** 2)
    return min_normal_weight, max_normal_weight


def main():
    try:
        # Ввод веса и роста в сантиметрах
        weight = float(input("Введите ваш вес (в килограммах): "))
        height_cm = float(input("Введите ваш рост (в сантиметрах): "))

        # Проверка на положительность значений
        if weight <= 0 or height_cm <= 0:
            raise ValueError("Вес и рост должны быть положительными числами.")

        # Рассчитываем ИМТ
        bmi = calculate_bmi(weight, height_cm)

        # Интерпретируем результат
        interpretation = interpret_bmi(bmi)

        # Вычисляем минимальный и максимальный нормальный вес
        min_normal_weight, max_normal_weight = calculate_weight_for_normal_bmi(height_cm)

        # Печатаем ИМТ и пояснение
        print(f"Ваш ИМТ: {bmi:.2f}")
        print(f"Пояснение: {interpretation}")

        # Если вес не в нормальном диапазоне, выводим, сколько нужно сбросить или набрать
        if weight < min_normal_weight:
            print(f"Чтобы попасть в нормальный вес, вам нужно набрать примерно {min_normal_weight - weight:.2f} кг.")
        elif weight > max_normal_weight:
            print(f"Чтобы попасть в нормальный вес, вам нужно сбросить примерно {weight - max_normal_weight:.2f} кг.")
        else:
            print("Ваш вес в пределах нормального диапазона.")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except ZeroDivisionError:
        print("Ошибка: рост не может быть равен нулю.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Запуск программы
if __name__ == "__main__":
    main()
