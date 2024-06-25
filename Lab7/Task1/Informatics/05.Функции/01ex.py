def funcMin(a, b, c, d):
    if a <= b and a <= c and a <= d:
        return a
    elif b <= a and b <= c and b <= d:
        return b
    elif c <= a and c <= b and c <= d:
        return c
    elif d <= a and d <= b and d <= c:
        return d
    



string = input()

numbers = [int(num) for num in string.split()]
x  = numbers[0]
y  = numbers[1]
z  = numbers[2]
k  = numbers[3]
ans = funcMin(x, y, z, k)

print(ans)