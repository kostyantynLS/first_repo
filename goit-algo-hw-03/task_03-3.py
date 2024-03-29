# Модуль 3. Завдання 3
# Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату, залишаючи тільки цифри та символ '+' на початку. Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі та перетворює його на стандартний формат, залишаючи тільки цифри та символ '+'. Якщо номер не містить міжнародного коду, функція автоматично додає код '+38' (для України). Це гарантує, що всі номери будуть придатними для відправлення SMS.

import re

def normalize_phone(phone_number) -> str:

    # перелік дозволених символів
    allowed = "+0123456789"
    # заміна символів
    phone_new = re.sub(r"[^+0123456789]", "", phone_number)

    if len(phone_new) == 9:
        phone_new = "0"+phone_new
    if len(phone_new) == 10:
        phone_new = "8"+phone_new
    if len(phone_new) == 11:
        phone_new = "3"+phone_new
    if len(phone_new) >= 12 and phone_new[0] != "+":
        phone_new = "+"+phone_new

#    if len(phone_new) >= 12 and phone_new[0] != "+":
#        phone_new = "+" + phone_new
#    if len(phone_new) == 10:
#        phone_new = "+38" + phone_new

    return phone_new
