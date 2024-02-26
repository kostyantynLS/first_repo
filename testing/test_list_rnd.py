import random 
#from random import *
print('type 2 values ',end="")
M,N = map (int, input().split())
print(M)
print(N)
a = [[(i*10+random.randint(1,10) ) for j in range(M)] for i in range(N)]

for i in range(M):
    print(a[i])
    print(sum (a[i]), print(min (a[i]) ))

s = "hello"
f=s.upper()
print(f,' ~ ',s)
h = list(s)
print(h)