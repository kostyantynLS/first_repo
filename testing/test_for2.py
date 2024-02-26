while False:
    for i in range(1, 10):
        if not (i % 2):
            print(f"{i} є парним числом.")
        else:
            print(f"{i} є непарним числом.")

h = [var for var in range(1,10)]
print(h)
for j in h:
    print(j**2, end =" ~ ")
print()

for h in range(0,10,2):
    print(h, end = " - ")
print()

