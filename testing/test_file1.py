fh = open('testfile.txt', mode='w+')
symbols_written = fh.write('hello!')
fh.seek(0)
first_two_symbols = fh.read(2)
print(symbols_written)
print(first_two_symbols)
fh.close()

fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
all_file = fh.read()
print(all_file)  # 'hello!'

fh.close()

fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol, end = " ")

fh.close()

fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)

fh.close()

'''
Зверніть увагу, що всі методи, які читають файли порядково,
залишають (не видаляють) символ перенесення рядка \n. 
Його, за необхідності, треба видаляти самостійно:
'''
fh = open("test.txt", "w")
fh.write("first line\nsecond line\nthird line")
fh.close()

fh = open("test.txt", "r")
lines = [el.strip() for el in fh.readlines()]
print(lines)

fh.close()

'''
Тепер повернемось до детального розгляду метода seek. Python дає можливість управляти положенням курсора (вказівника) у файлі та довільно переміщатися файлом за допомогою методу seek. Цей метод приймає один аргумент — це кількість символів, на які потрібно змістити курсор у файлі:
'''

fh = open('test.txt', 'w+')
fh.write('hello!')

fh.seek(1)
second = fh.read(1)
print(second)  # 'e'

fh.close()

'''
Щоб дізнатися положення курсора в цей момент, можна скористатися методом tell, він повертає позицію (номер) символу з початку файлу, де зараз знаходиться курсор.
'''

fh = open("test.txt", "w+")
fh.write("hello!")

position = fh.tell()
print(position)  # 6

fh.seek(1)
position = fh.tell()
print(position)  # 1

fh.read(2)
position = fh.tell()
print(position)  # 3

fh.close()


'''
Щоб уникнути цього, можна взяти блок коду, в якому відбувається робота з файлом, у блок try ... except:
'''
fh = open('text.txt', 'w+')
try:
    # Виконання операцій з файлом
    fh.write('Some data')
    fh.seek(0)
    text = fh.readline()
    print(text)
finally:
    # Закриття файлу в блоку finally гарантує, що файл закриється навіть у разі помилки
    fh.close()

'''
Для покращення читабельності коду при збереженні функціоналу можна скористатися менеджером 
контексту with. Менеджер контексту в Python - це спосіб використання ресурсів, 
який автоматично забезпечує правильне закриття файлу, незалежно від того, чи виникла 
помилка чи ні. Це робить код не тільки більш читабельним, але й безпечнішим.
'''
with open('text.txt', 'w') as fh:
    # Виконання операцій з файлом
    fh.write('Some data')
# Файл автоматично закриється після виходу з блоку with

with open("test.txt", "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open("test.txt", "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines)

