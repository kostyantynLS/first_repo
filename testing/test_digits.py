x = 9645
x_4 = x % 10
x_3 = (x//10) % 10
x_2 = (x//100) % 10
x_1 = (x//1000) % 10
print(x_4,x_3,x_2,x_1)

y = 0
avg = 0 

while x>0:
    y = y*10
    avg += x%10
    y = y + x%10
    x = x//10
print(avg/4,' ~ ',y)

def MyFunc(Name="Hi!", Ident=40):
    print(Name)
    print(Ident)

MyFunc()
MyFunc(Name="Text")

import datetime
#compare two dates

if datetime.datetime.strptime("2024-03-01", "%Y-%m-%d")<=datetime.datetime.now():
    print("We passed 2024.03.01 !!!!")
else:
    print(".... just wait some time")
