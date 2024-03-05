a = { 'max': 200 }
b = { 'min': 100, 'max': 250 }
c = { 'min': 50 }

g= a.get('min', 0) + b.get('min', 0) + c.get('min', 0) # 150
print(g)

g= a['min'] + b['min'] + c['min'] # throws KeyError
print(g)
