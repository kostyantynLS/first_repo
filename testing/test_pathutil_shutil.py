# Переміщення та копіювання файлів
# Для копіювання файлів використовується функція shutil.copy() або shutil.copy2().

import shutil
from pathlib import Path

# Вихідний і цільовий файли
source = Path('./my_directory/test.txt')
destination = Path('./my_directory/test2.txt')

# Копіювання файла
# shutil.copy(source, destination)

# Функція shutil.copy() копіює вміст файлу, але не копіює метадані, тоді як shutil.copy2() копіює і вміст, і метадані.
# Для переміщення файлів використовується функція shutil.move().

import shutil
from pathlib import Path

# Вихідний і цільовий шляхи
source = Path('./my_directory/test.txt')
destination = Path('./my_directory/test2.txt')

# Переміщення файла
# shutil.move(source, destination)

file_path = Path("./my_directory/test2.txt")

# Отримання розміру файла
size = file_path.stat().st_size
print(f"Розмір файла: {size} байтів")

# Час створення та модифікації
import time

creation_time = file_path.stat().st_ctime
modification_time = file_path.stat().st_mtime

print(f"Час створення: {time.ctime(creation_time)}")
print(f"Час модифікації: {time.ctime(modification_time)}")

'''
І остання необхідна інформація для роботи з файлами це видалення. 
Для видалення файлу використовується метод unlink(). Він видаляє файл, на 
який вказує об'єкт Path.
'''

# Path.unlink(missing_ok=False)

from pathlib import Path

# Створення об'єкту Path для файлу
file_path = Path('/path/to/file.txt')

# Перевірка, чи файл існує, перш ніж видаляти
if file_path.exists():
    file_path.unlink()
    print(f'Файл {file_path} було видалено')
else:
    print(f'Файл {file_path} не існує')

# Можна також видалити файл без попередньої перевірки його існування, використовуючи параметр missing_ok.
    
from pathlib import Path
file_path = Path('/path/to/file.txt')
file_path.unlink(missing_ok=True)
