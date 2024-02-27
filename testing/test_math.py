a = 4.1
b = 3
c = a**b
print(c)

a = 0.00003
b = 0.00004

c= (a**2+b**2)**0.5
print(f'side A {a}, side B {b}, side C {c}')

print(f"{a} + {b} = {a+b}".format(a,b))

import math

# Вихідне число
x = 3.7

# Використання різних методів округлення
ceil_result = math.ceil(x)  # Округлення вгору
floor_result = math.floor(x)  # Округлення вниз
trunc_result = math.trunc(x)  # Відсікання дробової частини

print(ceil_result, floor_result, trunc_result)

import math

r = math.isclose(0.1, 0.10000000009)
print(r)  # Це поверне True

import time, datetime

print(time.time())

datetime.timedelta()

print(math.sqrt(4))


#swapping

a = 10
b = 20
print(a,b)

a, b = b, a

print(a,b)
