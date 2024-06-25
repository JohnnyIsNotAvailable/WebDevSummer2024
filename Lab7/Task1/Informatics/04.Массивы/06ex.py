numbers = [int(num) for num in input().split()]

count = 0
for i in range(1, len(numbers) - 1):  # Exclude first and last elements
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        count += 1

print(count)