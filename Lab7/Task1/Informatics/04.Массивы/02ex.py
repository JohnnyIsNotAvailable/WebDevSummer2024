string = input()

numbers = [int(x) for x in string.split()]

i = 0

while True:
    try:
        if numbers[i] % 2 == 0:
            print(numbers[i], end = ' ')

        i += 1
    except:
        break
