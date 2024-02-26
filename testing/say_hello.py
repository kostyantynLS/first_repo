def say_hello():
		# тіло функції
    print('Привіт, Світ!')

# Кінець функції say_hello()

# виклик функції
say_hello()

# ще один виклик функції
say_hello()


def print_max(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів

def is_even(num: int) -> bool:
    return num % 2 == 0

check_even = is_even(4)
print(check_even)  # Виведе: True

def modify_string(original: str) -> str:
    original = "змінено"
    return original

str_var = "оригінал"
print(modify_string(str_var))  # виведе: змінено
print(str_var)                # виведе: оригінал

def modify_list(lst: list) -> None:
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3, 4]


def string_to_codes(string: str) -> dict:
    # Ініціалізація словника для зберігання кодів
    codes = {}  
    # Перебір кожного символу в рядку
    for ch in string:  
        # Перевірка, чи символ вже є в словнику
        if ch not in codes:
            # Додавання пари символ-код в словник  
            codes[ch] = ord(ch)  
    return codes

msg = "My long message about love"
eDic = string_to_codes(msg)
print(eDic)

