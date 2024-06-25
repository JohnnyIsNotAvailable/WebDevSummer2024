x = int(input())
y = 0
cnt = len(str(x))
# cnt2 = x
# while cnt2 != 0:
#     cnt += 1
#     cnt2 = cnt2 // 10

for i in range(0, cnt):
    y += (x % 10) * 2 ** i 
    x = x // 10

print(y)