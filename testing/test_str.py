cat = {}
info = {"status": "vaccinated", "breed": True}
for x in info:
    print(x, " ~> ", info.get(x))
    cat[x] = info.get(x)
    print(x,' -> ', cat.get(x))

print(cat)
if (cat == info):
    print('cat and info equal each other')
msg = "equal" if cat == info else "not equal"
print('cat and info',msg,'each other')

is_nice = True
state = "nice" if is_nice else "not nice"
print(state)

fruit = "apple"
match fruit:
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "orange":
        print("This is an orange.")
    case _:
        print("Unknown fruit.")


my_tuple = tuple()
print(my_tuple)
my_tuple = (1,2,3)
print(my_tuple)
my_tuple = (1,2,3,5,6,7)
print(my_tuple)
my_tuple = my_tuple + (1,2)
print(my_tuple)

points = {
    (0, 0): "O",
    (1, 1): "A",
    (2, 2): "B"
}
print(points[(0,0)])


print('type ENTER to exit')
while True:
    ks = input('x=')
    if ks:
        kx = int(ks)
    else:
        break;
    ks = input('y=')
    if ks:
        ky = int(ks)
    else:
        break;
    point = (kx, ky)
    match point:
        case (0, 0):
            print("Точка в центрі координат")  
        case (0, y):
            print(f"Точка лежить на осі Y: y={y}")  
        case (x, 0):
            print(f"Точка лежить на осі X: x={x}") 
        case (x, y):
            print(f"Точка має координати:  x={x}, y={y}") 
        case _:
            print("Це не точка")

