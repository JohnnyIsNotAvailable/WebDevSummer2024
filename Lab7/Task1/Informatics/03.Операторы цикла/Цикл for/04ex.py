def countDigits(x, d):
  if x < 0:
    return 0

  count = 0
  while x:
    if x % 10 == d:
      count += 1
    x //= 10
  return count


x = int(input())
d = int(input())

numberOfDigits = countDigits(x, d)

# Выводим результат
print(numberOfDigits)
