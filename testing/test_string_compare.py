string1 = "Hello World"
string2 = "hello world"
if string1.lower() == string2.lower():
    print("Рядки однакові")
else:
    print("Рядки різні")

'''
Щоб розв'язати цю проблему при роботі з не ASCII символами для порівняння рядків, 
їх необхідно нормалізувати за допомогою методу casefold, який повертає рядок, де всі символи 
у нижньому регістрі і без неоднозначностей, коли будь-який символ матиме тільки одну 
можливу форму запису.

Цей метод схожий на lower(), але casefold() є більш радикальним: він призначений 
для видалення усіх відмінностей у регістрі, які можуть виникати в різних мовах, і 
тому є більш ефективним для випадків, де потрібно забезпечити нерозрізнення регістру в 
різноманітних мовах.
'''

text = "Python Programming"
print(text.casefold())

german_word = 'straße'  # В нижньому регістрі
search_word = 'STRASSE'  # В верхньому регістрі

# Порівняння за допомогою lower()
lower_comparison = german_word.lower() == search_word.lower()

# Порівняння за допомогою casefold()
casefold_comparison = german_word.casefold() == search_word.casefold()

print(f"Порівняння з lower(): {lower_comparison}")
print(f"Порівняння з casefold(): {casefold_comparison}")

