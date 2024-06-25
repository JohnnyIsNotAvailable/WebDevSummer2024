x = int(input())

minDiv = 2

for i in range(0, x + 1):
    if x % minDiv == 0:
        print(minDiv)
        break
    else:
        minDiv += 1    
    

