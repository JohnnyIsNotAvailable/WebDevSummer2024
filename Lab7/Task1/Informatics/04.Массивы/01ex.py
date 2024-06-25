string = input()

numbers = [int(x) for x in string.split()]
ans = [numbers[::2]]
i = 0

while True:
    try:
        if i % 2 == 0:
            print(numbers[i], end = ' ')

        i += 1
    except:
        break

# for num in numbers:
#     if num % 2 == 0:
#         ans.append(numbers[num])



# ", ".join(map(str, numbers)