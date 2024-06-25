string = input()

numbers = [int(x) for x in string.split()]

i = 0
cnt = 0
while True:
    try:
        if numbers[i] > 0:
            cnt += 1

        i += 1
    except:
        break

print (cnt)