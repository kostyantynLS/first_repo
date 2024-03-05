# Робота з не текстовими файлами у Python

with open('raw_data.bin', 'wb') as fh:
    fh.write(b'Hello world!')

s = b'Hello!'
print(s[1])  # Виведе: 101 (це ASCII-код символу 'e')

print(s[2])  # Виведе: 108 (це ASCII-код символу 'l')

byte_string = b'Hello world!'

'''
Для перетворення рядка у байт-рядок можна скористатися методом рядків encode. 
Коли ви використовуєте .encode(), ви перетворюєте рядок у байтову послідовність. 
Метод .encode() важливий, оскільки він дозволяє стандартизувати рядок для операцій, 
які вимагають однакового представлення символів, незалежно від системи або платформи.
'''
byte_str = 'some text'.encode()
print(byte_str)

#str.encode(encoding="utf-8", errors="strict")

# Перетворення списку чисел у байт-рядок
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)  # Виведе байтове представлення чисел

for num in [127, 255, 156]:
  print(hex(num))

# Кодування рядків (ASCII, UTF-8, CP1251)

print(ord('a'))  # 97

print(chr(128))  # 'd'

s = "Привіт!"

utf8 = s.encode()
print(f"UTF-8: {utf8}")

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)

print(b'Hello world!'.decode('utf-16'))

'''
Щоб уникнути проблем з кодуванням, особливо при роботі з міжнародними текстами 
або в середовищах з різними налаштуваннями кодування, рекомендується завжди явно 
вказувати кодування UTF-8 під час відкриття файлів у Python. Це можна зробити 
за допомогою параметра encoding у функції open().
'''

# Відкриття текстового файлу з явним вказівкам UTF-8 кодування
with open('example.txt', 'w+', encoding='utf-8') as file:
    file.write('Привіт!')
    file.seek(0)
    content = file.read()
    print(content)

'''
Робота з рядками обмежена тим, що рядки і байт-рядки незмінні. 
Якщо потрібно замінити навіть один символ, потрібно, по суті, створити 
копію початкового рядка з єдиним відмінним символом. Щоб зменшити 
накладні витрати при роботі з "сирими" даними, в Python є такий контейнер як bytearray.
'''

byte_array = bytearray(b'Kill Bill')
byte_array[0] = ord('B')
byte_array[5] = ord('K')
print(byte_array)

byte_array = bytearray(b"Hello")
byte_array.append(ord("!"))  
print(byte_array)

'''
Хоча bytearray сприймається як послідовність чисел, його можна легко перетворити 
в рядок за допомогою методу decode(), вказавши потрібне кодування.
'''

byte_array = bytearray(b"Hello World")
string = byte_array.decode("utf-8")
print(string)  # Виведе: 'Hello World'
