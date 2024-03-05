from pathlib import Path

# Створення об'єкту Path для директорії
directory = Path(".")

# Виведення переліку всіх файлів та піддиректорій
for path in directory.iterdir():
    print(path)

'''
Для створення нової директорії використовується метод mkdir().

Параметри:
mode - права доступу до директорії, використовуються для Linux і не актуальні для Windows.
parents - якщо має значення True, створить всі батьківські директорії, які відсутні.
exist_ok - якщо має значення True, помилка не буде викинута, якщо директорія вже існує.
'''

from pathlib import Path
directory = Path('./my_directory/new_folder')
directory.mkdir(parents=True, exist_ok=True)
input('press enter to go...')

directory = Path('./my_directory/new_folder')
directory.rmdir()

'''
метод exists() перевіряє, чи існує файл або директорія.
метод is_dir() перевіряє, чи є об'єкт директорією.
метод is_file() перевіряє, чи є об'єкт файлом.
'''

from pathlib import Path

path = Path("./my_directory")

# Перевірка існування
if path.exists():
    print(f"{path} існує")
else:
    print(f'{path} не існує')

# Перевірка, чи це директорія
if path.is_dir():
    print(f"{path} є директорією")
else:
    print(f'{path} не є директорією')


# Перевірка, чи це файл
if path.is_file():
    print(f"{path} є файлом")
else:
    print(f"{path} не є файлом")

