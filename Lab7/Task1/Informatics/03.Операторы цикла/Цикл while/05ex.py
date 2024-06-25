def isWork():
    if i**2 > x:
        return False
    
    return True

x = int(input())

i = 0

while 2 ** i < x:
    i += 1

print(i)