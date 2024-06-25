def countZeros(numbers):

  count = 0
  for number in numbers:
    if number == 0:
      count += 1
  return count

n = int(input())

numbers = [int(input()) for _ in range(n)]

zeroCount = countZeros(numbers)

print(zeroCount)
