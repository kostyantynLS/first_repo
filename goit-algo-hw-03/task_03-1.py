# Модуль 3. Завдання 1
# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

import datetime

def get_days_from_today(date) -> int:
    # перевірка дати
    try:
        d_ask = datetime.datetime.strptime(date,"%Y-%m-%d")
    except ValueError:
        print("get_days_from_today() : Incorrect date format")
        return -1
    # отримання поточної дати
    d_now = datetime.datetime.today()

    # для перевірки дати згідно тестового завдання
    # d_now = datetime.datetime.strptime("2021-05-05", "%Y-%m-%d")

    # переведення дат у число днів
    day_from = datetime.date.toordinal(d_ask)
    day_to = datetime.date.toordinal(d_now)

    # обрахунок кількості днів з врахуванням дата у минулому або майбутньому часі
    # знак результату не вимагається згідно завдання
    date_days = abs(day_from - day_to)

    return date_days

# перевірка роботи
#print(get_days_from_today("2021-10-09"))
#print(get_days_from_today("2021h10-k9"))
#print(get_days_from_today("2а23-10_09"))
