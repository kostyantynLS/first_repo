text = """This is first line
And second line
Last third line"""

song = '''Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh'''

print(text)
print()
print(song)



s = "Hi there!"
start = 0
end = 7
print(s.find("er", start, end)) # 5
print(s.find("q")) # -1

s = 'Some words'
print(s.find("o"))
print(s.rfind('o'))

s = 'Some words'
print(s.index("o"))
print(s.rindex('o'))

text = "hello world"
result = text.split()
print(result)  # Виведе: ['hello', 'world']

text = "apple,banana,cherry"
result = text.split(',')
print(result)  # Виведе: ['apple', 'banana', 'cherry']

result = ' '.join(result)
print(result)

text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text) 

text = "one fish, two fish, red fish, blue fish"
new_text = text.replace("fish", "bird", 2)
print(new_text)  

print('TestHook'.removeprefix('Test')) # Hook
print('TestHook'.removeprefix('Hook')) # TestHook
print('TestHook'.removesuffix('Test')) # TestHook
print('TestHook'.removesuffix('Hook')) # Hook

print("/n"*2)

url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)

number = "12345"
print(number.isdigit())  # Виведе: True

text = "Number123"
print(text.isdigit())  # Виведе: False

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "This is string example"
print(str.translate(trantab))

intab = "aeiou"
trantab = str.maketrans('', '', intab)

#Метод translate() також може використовуватися для видалення певних символів із рядка. 
#Для цього передайте в maketrans() третій аргумент - рядок символів, які потрібно видалити.
str = "This is string example"
print(str.translate(trantab))

#Наприклад нам треба розробити програму, яка конвертує рядок, що містить шістнадцяткові числа (в якості окремих символів), у відповідний двійковий код.
symbols = "0123456789ABCDEF"
code = [
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
        ]

MAP = {}

for s, c in zip(symbols, code):
    MAP[ord(s)] = c
    MAP[ord(s.lower())] = c

print(MAP)

result = "34 DF 56 AC".translate(MAP)
print(result)

#Наступний приклад, це розробити програму, яка перетворює вхідний текстовий рядок на відповідний код мови Морзе.
morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}

# Перетворення ключів словника на Unicode коди
table_morze_dict = {}
for k, v in morze_dict.items():
    table_morze_dict[ord(k)] = v

string = "Hello world"

result = ""

for ch in string:
    result = result + ch.upper().translate(table_morze_dict)

print(result)



