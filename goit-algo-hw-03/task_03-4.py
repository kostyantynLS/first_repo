# Модуль 3. Завдання 4
# створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати

import datetime

def get_upcoming_birthdays(user_list) -> dict:

    # створюємо список для результатів
    birth_list = list()

    # поточна дата
    date_curr = datetime.datetime.today()

    # обробляємо перелік користувачів та дат
    for line in user_list:

        # визначаємо словник з вхідного списку
        dic = dict(line)

        # визначаємо ім'я користувача
        name = dic["name"]

        # визначаємо дату народження в форматі datetime
        birth = dic["birthday"]

        # конвертуємо дату дня народження
        try:
            date_birth = datetime.datetime.strptime(birth, "%Y.%m.%d")
        except ValueError:
            # повідомлення про помилку в даті
            print(f"get_upcoming_birthdays() : {name} have invalid birthday {birth}")
        # пропускаємо помилковий запис і йдемо до іншого
            continue

        # конвертуємо дату народження до поточного року
        date_curr_year =  int(date_curr.strftime("%Y"))
        date_birth_new = datetime.datetime.strptime( \
            str(date_curr_year)+"."+date_birth.strftime("%m.%d"),"%Y.%m.%d")        

        # Перевірка, чи вже минув день народження в цьому році
        # Якщо минув, рухаємо дату на наступний рік.
        if date_birth_new < date_curr:
            date_curr_year += 1
            date_birth_new = datetime.datetime.strptime( \
                str(date_curr_year)+"."+date_birth.strftime("%m.%d"),"%Y.%m.%d")        

        #Визначаємо різницю між днем народження та поточним днем для визначення днів народження на наступний тиждень.
        date_diff = date_birth_new.toordinal() - date_curr.toordinal()

        if date_diff <= 7:
            # оголошуєму пустий словник
            birth_user = dict()
            
            # додаємо ключ ІМЯ
            birth_user["name"] = name

            # визначаємо день, на який припадає день народження
            # якщо день народження на вихідний день (НЕДІЛЯ), то привітання на ПОНЕДІЛОК
            if date_birth_new.weekday() == 6:
                date_birth_new = date_birth_new + datetime.timedelta(days=1)
            
            # записуємо день привітання з днем народження
            birth_user["birth_holiday"] = date_birth_new.strftime("%Y.%m.%d")

            # додаємо до списку словник для привітання
            birth_list.append(birth_user)

    return birth_list

# users = [
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "William Xing", "birthday": "1985.02.28"},
#     {"name": "Anna Bing", "birthday": "1982.03.03"},
#     {"name": "Mondi Wood", "birthday": "1987.06.33"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}
# ]

# upcoming_birthdays = get_upcoming_birthdays(users)
# print("Список привітань на цьому тижні:", upcoming_birthdays)
