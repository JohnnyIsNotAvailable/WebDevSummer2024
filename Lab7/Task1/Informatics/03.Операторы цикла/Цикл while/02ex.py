def isWork():
    if i**2 > x:
        return False
    
    return True

x = int(input())

i = 2

while True:
    
    if x % i == 0:
        print(i)
        break
    i += 1