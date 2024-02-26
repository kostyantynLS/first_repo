while False:
    fruit = 'apple'
    vegs = set(fruit)
    print(vegs)

    for char in vegs:
        print(char)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        print(char, end=" ")
    print

some_iterable = ["a", "b", "c"]
for i in some_iterable:
    print(i)

odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(i ** 2)

# Зчитування рядка від користувача
user_input = input("Введіть рядок: ")

# Ініціалізація змінних для підрахунку символів та пробілів
total_chars = len(user_input)  # загальна кількість символів у рядку
space_count = 0  # кількість пробілів

# Підрахунок кількості пробілів
for char in user_input:
    if char == " ":
        space_count += 1

# Виведення результатів
print(f"Загальна кількість символів у рядку: {total_chars}")
print(f"Кількість пробілів у рядку: {space_count}")

a = 0
while a < 6:
    a = a + 1
    if not a % 2:
        continue
    print(a)
