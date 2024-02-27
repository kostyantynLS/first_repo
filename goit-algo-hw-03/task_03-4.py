# Модуль 3. Завдання 4
# створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати

import datetime

def get_upcoming_birthdays(user_list) -> dict:

    birth_list = list()

    # поточна дата
    date_curr = datetime.datetime.today()

    # обробляємо перелік користувачів та дат
    for line in user_list:
        # визначаємо словник з вхідного списку
        dic = dict(line)
        name = dic["name"]
        birth = dic["birthday"]

        # конвертуємо дату дня народження
        try:
            date_birth = datetime.datetime.strptime(birth, "%Y.%m.%d")
        except ValueError:
            print(f"get_upcoming_birthdays() : {name} have invalid birthday {birth}")
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
            birth_user = dict()
            birth_user["name"] = name

            # визначаємо день, на який припадає вітання
            wd = date_birth_new.weekday()
            if wd >= 5:
                print('!!', wd)
                date_birth_new = date_birth_new + datetime.timedelta(days=7-wd)
            
            # записуємо день привітання з днем народження
            birth_user["birth_holiday"] = date_birth_new.strftime("%Y.%m.%d")
            birth_list.append(birth_user)

    return birth_list
