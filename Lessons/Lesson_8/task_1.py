"""
Task_1
Реализовать программу для подсчёта индекса массы тела человека.
Пользователь вводит рост и вес с клавиатуры.
На выходе – ИМТ и пояснение к нему в зависимости от попадания в тот или иной диапазон.
Использовать обработку исключений.
"""


def calculate_imt(weight, height_cm):
    """Функция для расчёта индекса массы тела (ИМТ)"""
    height_m = height_cm / 100  # Переводим рост из сантиметров в метры
    return weight / (height_m ** 2)


def interpret_imt(imt):
    """Функция для интерпретации ИМТ"""
    if imt < 18.5:
        return "Недостаточный вес"
    elif 18.5 <= imt < 25:
        return "Нормальный вес"
    elif 25 <= imt < 30:
        return "Избыточный вес"
    else:
        return "Ожирение"


def calculate_weight_for_normal_imt(height_cm):
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
            raise ValueError("Вес и рост должен быть больше 0")

        # Рассчитываем ИМТ
        imt = calculate_imt(weight, height_cm)

        # Интерпретируем результат
        interpretation = interpret_imt(imt)

        # Вычисляем минимальный и максимальный нормальный вес
        min_normal_weight, max_normal_weight = calculate_weight_for_normal_imt(height_cm)

        # Печатаем ИМТ и состояние тела
        print(f"Ваш ИМТ: {imt:.2f}")
        print(f"Состояние тела: {interpretation}")

        # Если вес не в нормальном диапазоне, выводим, сколько нужно сбросить или набрать
        if weight < min_normal_weight:
            print(f"Для нормального веса вам нужно набрать примерно {min_normal_weight - weight:.2f} кг.")
        elif weight > max_normal_weight:
            print(f"Для нормального веса вам нужно сбросить примерно {weight - max_normal_weight:.2f} кг.")
        else:
            print("Ваш вес в пределах нормального диапазона")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except ZeroDivisionError:
        print("Ошибка: рост не может быть равен нулю")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
