empty_dict = {}
user = {'first_name': "Henry", 
        'last_name': 'Smith',
        'age': 25,
        'data': None,
        'bool': True,
        (1,2,): 'huge_key',
        'dict': {
            1: 55,
            3.5: 334}
        }
print(user)

first = {'a22': 10, 'b': 20}
second = {'b': 'other'}

first.update(second)
print(first)

print(first['a22'])
print(first.get('c'))
first['b'] = 'updated value'
print(first['b'])
print(first.items())

my_set = set(first)
print(my_set)