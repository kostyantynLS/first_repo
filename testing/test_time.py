import time

current_time = time.time()
print(f"Поточний час: {current_time}")

print("Початок паузи")
time.sleep(2)
print("Кінець паузи")

current_time = time.time()
print(f"Поточний час: {current_time}")
readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}")

import time

current_time = time.time()
print(f"Поточний час: {current_time}")

local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}")

#Давайте використаємо time.perf_counter() для вимірювання часу виконання деякого блоку коду:
import time

# Записуємо час на початку виконання
start_time = time.perf_counter()

# Виконуємо якусь операцію
for _ in range(1_000_000):
    pass  # Просто проходить цикл мільйон разів

# Записуємо час після виконання операції
end_time = time.perf_counter()

# Розраховуємо та виводимо час виконання
execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")

import random

fill_percentage = random.random() * 100
print(f"Заповнення: {fill_percentage:.2f}%")


import random

cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]

for g in range(1,6):
    random.shuffle(cards)
    print(f"Перемішана колода №{g}: {cards}")

import random

items = ['яблуко', 'банан', 'вишня', 'диня']
for g in range(1,6):
    chosen_item = random.choices(items, k=1)
    print(chosen_item)  

import random
#Вибір декількох елементів з можливістю повторень:
numbers = [1, 2, 3, 4, 5]
chosen_numbers = random.choices(numbers, k=3)
print(chosen_numbers)

#Вибір з вагами:
import random

colors = ['червоний', 'зелений', 'синій']
weights = [10, 1, 1]
chosen_color = random.choices(colors, weights, k=1)
print(chosen_color)  

#random.choices() - це гнучкий метод для створення випадкових вибірок з можливістю зазначення ймовірностей для кожного елемента та можливістю повторень у вибірці.
#Якщо виникає необхідність вибрати N елементів зі списку і вони при цьому не повторювалися треба використати метод random.sample(population, k). Він повертає список довжиною k з унікальними елементами, вибраними випадково з population.
#Створення випадкової команди з 4 учасників з групи з 10 осіб:

import random

participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
team = random.sample(participants, 4)
print(f"Команда: {team}")

#Приклад генерації випадкової ціни для продукту в межах від 50 до 100:
import random

price = random.uniform(50, 100)
print(f"Випадкова ціна: {price:.2f}")

