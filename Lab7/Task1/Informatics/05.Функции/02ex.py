# def funcMin(a, b, c, d):
#     if a <= b and a <= c and a <= d:
#         return a
#     elif b <= a and b <= c and b <= d:
#         return b
#     elif c <= a and c <= b and c <= d:
#         return c
#     elif d <= a and d <= b and d <= c:
#         return d
    
def doublePower(a: float, b: int):
    # if b == 0:
    #     return 1
    # elif b % 2 == 0:
    #     return doublePower(a * a, b // 2)
    # else:
    #     return a * doublePower(a * a, (b - 1) // 2)
    return a ** b


string = input()

numbers = [int(num) for num in string.split()]
x  = float(numbers[0])
y  = numbers[1]

ans = float(doublePower(x, y))

print(ans)