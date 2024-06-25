def isCorrectAnswer(systemAnswer, studentAnswer):
  if systemAnswer == 1:
    return studentAnswer == 1
  else:
    return systemAnswer != 1 and studentAnswer != 1

systemAnswer = int(input())
studentAnswer = int(input())

if isCorrectAnswer(systemAnswer, studentAnswer):
  print("YES")
else:
  print("NO")
