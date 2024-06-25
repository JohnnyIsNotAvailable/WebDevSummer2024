def countDivisors(n):

  if n <= 1:
    return n

  count = 2  
  sqrt_n = int(n ** 0.5)  
  i = 2
  while i <= sqrt_n:
    if n % i == 0:
      count += 1
      if i * i != n:
        count += 1
    i += 1
  return count

number = int(input())


divisors = countDivisors(number)


print(divisors)
