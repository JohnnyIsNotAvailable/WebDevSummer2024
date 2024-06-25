def isWork():
    if i**2 > x:
        return False
    
    return True

x = int(input())

i = 0

while True:
    
    if 2 ** i > x:
        break
    else:
        print(2**i)
    i += 1