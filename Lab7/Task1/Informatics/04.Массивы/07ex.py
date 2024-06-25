numbers = [int(num) for num in input().split()]

max_value = numbers[0]  # Initialize with first element
max_index = 0

for i in range(1, len(numbers)):
    if numbers[i] > max_value:
        max_value = numbers[i]
        max_index = i

print(max_value, max_index)