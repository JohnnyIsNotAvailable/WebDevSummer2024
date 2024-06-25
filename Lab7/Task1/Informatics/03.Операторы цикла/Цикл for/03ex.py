from math import sqrt 
x = int(input())
y = int(input())


for  i in range(x,y+1):
    if sqrt(i) % 1 == 0:
        print(i, end = " ")