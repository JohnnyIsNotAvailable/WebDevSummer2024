def isWork():
    if i**2 > x:
        return False
    
    return True

x = int(input())

i = 2

while True:
    
    if x == 1:
        print("YES")
        break

    if x < 1 :
        print("NO")
        break
    
    x = x / 2