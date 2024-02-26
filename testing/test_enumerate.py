some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)

for j in some_list:
    print(j, some_list.index(j))

list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)

for some in list1:
    print(some, list2[list1.index(some)])

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']
for number, letter in zip(list1, list2):
    print(number, letter)

for some in range(0, min(len(list1), len(list2))):
    print(list1[some], list2[some])

print(list2.count('a'))