'''
Окрім роботи з архівами модуль shutil може ще виконувати наступні високорівневі операції для обробки файлової системи:

shutil.copy(src, dst) копіює файл з src в dst. Якщо dst є директорією, файл буде скопійований зі своїм поточним іменем у цю директорію.
shutil.copytree(src, dst) рекурсивно копіює всю директорію src в директорію dst.
shutil.move(src, dst) переміщує файл або директорію src в dst.
shutil.rmtree(path) рекурсивно видаляє директорію path.
shutil.disk_usage(path) повертає статистику використання диска, що містить загальний об'єм, використаний об'єм і вільний об'єм для даного шляху.


import shutil

# Копіюємо файл
source_file = '/path/to/source/file.txt'
destination_dir = '/path/to/destination'
shutil.copy(source_file, destination_dir)

# Копіюємо всю директорію
source_dir = '/path/to/source/directory'
destination_dir = '/path/to/destination/directory'
shutil.copytree(source_dir, destination_dir)
'''

'''
pathlib - це модуль у Python, який надає класи для обробки файлових шляхів у об'єктно-орієнтованому стилі. Два основних класи у цьому модулі - це Path та PurePath.
PurePath - це базовий клас у pathlib, який надає об'єктно-орієнтовані методи для маніпуляції шляхами без доступу до файлової системи. Він може бути використаний для роботи з шляхами на різних операційних системах. PurePath дозволяє виконувати такі операції, як розділення шляху на частини, перевірка суфіксів, імен файлів, шляхів тощо.
'''

from pathlib import PurePath

p = PurePath("/usr/bin/simple.jpg")
print("Name:", p.name)  
print("Suffix:", p.suffix) 
print("Parent:", p.parent)

from pathlib import Path

p = Path("example2.txt")
p.write_text("Hello, world!")
print(p.read_text()) 
print("Exists:", p.exists()) 

'''
Створення шляхів за допомогою класу Path у модулі pathlib у Python 
є зручним способом маніпуляції файловими шляхами, який абстрагує від 
особливостей конкретної операційної системи.

Клас Path автоматично адаптується до особливостей шляхів у різних 
операційних системах. Наприклад, у Windows використовуються зворотні 
слеші (\), тоді як в Unix-подібних системах (Linux, macOS) - прямі слеші (/).
'''

from pathlib import Path

# Для Windows
path_windows = Path("C:/Users/Username/Documents/file.txt")

from pathlib import Path
# Початковий шлях
base_path = Path("/usr/bin")
# Додавання додаткових частин до шляху
full_path = base_path / "subdir" / "script.py"
print(full_path)  # Виведе: /usr/bin/subdir/script.py

from pathlib import Path

# Перетворення відносного шляху в абсолютний
relative_path = Path("documents/example.txt")
absolute_path = relative_path.absolute()
print(absolute_path)


try:
    from pathlib import Path
    # Перетворення відносного шляху в абсолютний
    relative_path = Path("documents/example.txt")
    absolute_path = relative_path.absolute()
    current_working_directory = Path("C:\MyProject\Python\python-help-solution\example_for_new_core\l04")
    relative_path = absolute_path.relative_to(current_working_directory)
    print(relative_path)
except Exception as e:
    print(f'exception {e} at module Pathlib')

print()

from pathlib import Path
# Початковий шлях до файлу
original_path = Path("documents/example.txt")
# Зміна імені файлу
new_path = original_path.with_name("report.txt")
print(new_path)

from pathlib import Path

# Початковий шлях до файлу
original_path = Path("documents/example.txt")
# Зміна імені файлу
new_path = original_path.with_suffix(".md")
print(new_path)

# Path.read_text(encoding=None, errors=None)
# Path.write_text(data, encoding=None, errors=None)

'''
Як бачимо параметр errors, в обох методах, визначає, як мають бути оброблені ці помилки.

errors='strict'. Це значення за замовчуванням. Якщо виникає помилка декодування, 
буде викинуто виключення UnicodeDecodeError.
errors='ignore'. Якщо ми хочемо ігнорувати помилки декодування. Частини тексту, 
що не можуть бути декодовані, будуть просто пропущені.
errors='replace'. Якщо пропускати ми не хочемо, то замінимо неможливі для 
декодування символи на спеціальний символ заміни, згідно документації символ '?'.
'''

from pathlib import Path

# Створення об'єкту Path для файлу
file_path = Path("example3.txt")

# Запис тексту у файл
file_path.write_text("Привіт світ! utf-8 !", encoding="utf-8")

# Читання тексту з файлу
text = file_path.read_text(encoding="utf-8")
print(text)

# Приклад запису бінарних даних у файл
# 
from pathlib import Path

# Створення об'єкту Path для бінарного файлу
file_path = Path("example.bin")
# Бінарні дані для запису
data = b"Python is great!"
# Запис байтів у файл
file_path.write_bytes(data)

file_path = Path("example.bin")

# Читання байтів з файлу
binary_data = file_path.read_bytes()
print(binary_data)
