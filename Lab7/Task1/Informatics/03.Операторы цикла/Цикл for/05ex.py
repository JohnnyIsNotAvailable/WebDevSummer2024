x = int(input())

summ = 0

while x!= 0:
    d = x % 10
    summ += d

    x = x//10

print(summ)