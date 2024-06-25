string = input()

numbers = [int(x) for x in string.split()]

i = 0
cnt = 0
while True:
    try:
        if numbers[i + 1] == None:
            break
        if numbers[i] < numbers[i + 1]:
            print (numbers[i + 1], end = ' ')
        i += 1

    except:
        break
