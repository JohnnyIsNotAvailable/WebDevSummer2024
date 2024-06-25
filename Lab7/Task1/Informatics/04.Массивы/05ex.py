# string = input()

# numbers = [int(x) for x in string.split()]

# i = 0
# cnt = 0
# while True:
#     try:
#         if numbers[i + 1] == None:
#             break
#         if numbers[i] + 1 == numbers[i + 1]:
#             print (numbers[i], numbers[i + 1])
#             break
#         i += 1

#     except:
#         break

numbers = [int(num) for num in input().split()]
i = 0
while i < len(numbers) - 1:
    current_num = numbers[i]
    next_num = numbers[i + 1]

    if current_num * next_num > 0:  # Same sign (positive or negative)
        print(current_num, next_num)
        break  # Exit loop after finding the first pair

    i += 1

# if i == len(numbers) - 1:  # Reached the end without finding a pair
#     print("No consecutive pairs of same sign found.")