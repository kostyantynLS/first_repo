# Модуль 3. Завдання 2
# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.

import random

def get_numbers_ticket(min, max, quantity) -> list:

    # перевірка коректності вхідних умов
    if max<1 or min<1 or quantity<1:
        print("get_numbers_ticket() : Only positive values")
        return list()
    if (max+1)<=(min+quantity):
        print("get_numbers_ticket() : Low range MIN to MAX")
        return list()

    # bil - кількість квитків
    bil = quantity

    # tickets_set - набір випадкових чисел
    tickets_set = []

    # основний цикл
    while bil>0:
        # генерування випадкового номеру квитка, діапазон (min, max) включно
        gen_tick = random.randint(min, max)
        # перевірка наявності числа у списку
        if not gen_tick in tickets_set:
            # немає у списку, то додаємо
            tickets_set.append(gen_tick)
            bil -= 1

    # переводимо множину у список
    tickets_list = list(tickets_set)

    # сортування списку
    tickets_list.sort()

    # або просто return tickets_list.sort()
    return tickets_list

print(get_numbers_ticket(10,  4, 5))
print(get_numbers_ticket(10, 14, 6))