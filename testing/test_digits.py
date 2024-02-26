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