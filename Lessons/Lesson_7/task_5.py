"""
Task_5
Используя map() и reduce() посчитать площадь
квартиры, имея на входе характеристики комнат квартиры.
Пример входных данных:
rooms = [
{"name": ”Kitchen", "length": 6, "width": 4},
{"name": ”Room 1", "length": 5.5, "width": 4.5},
{"name": ”Room 2", "length": 5, "width": 4},
{"name": ”Room 3", "length": 7, "width": 6.3},
]
"""

from functools import reduce


def get_room_data(name):
    """Функция: Спрашивает у пользователя длину и ширину комнат в метрах"""
    length = float(input(f"Введите длину комнаты '{name}' в метрах: "))
    width = float(input(f"Введите ширину комнаты '{name}' в метрах: "))
    return {"name": name, "length": length, "width": width}


def main():
    """Функция: Спрашивает у пользователя сколько комнат в квартире, выводит общую площадь квартиры"""
    num_rooms = int(input("Введите количество комнат в квартире(кроме кухни и коридора): "))

    rooms = [get_room_data("Kitchen"), get_room_data("Corridor")]

    # Добавление остальных комнат
    for i in range(1, num_rooms + 1):
        rooms.append(get_room_data(f"Room {i}"))

    # Вычисление площади каждой комнаты
    areas = map(lambda room: room["length"] * room["width"], rooms)

    # Вычисление общей площади квартиры
    total_area = reduce(lambda x, y: x + y, areas)

    # Вывод пользователю результата подсчетов общей площади квартиры
    print(f"Общая площадь квартиры: {total_area:.2f} кв. метра")


if __name__ == "__main__":
    main()
