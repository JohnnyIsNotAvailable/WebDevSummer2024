def xor(x: bool, y: bool) -> bool:
    return x != y
    
# string = input()

# numbers = [int for num in string.split()]

# x = bool(numbers[0])
# y = bool(numbers[1])

input_values = input().split()

x = bool(int(input_values[0]))
y = bool(int(input_values[1]))

ans = xor(x, y)

print(ans)