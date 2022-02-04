# 291/305 тестов
def myPow(self, x, n):
  ans = 1
  if n > 0:
    for i in range(n):
      ans *= x
    return ans
  else:
    x = 1 / x
    for i in range(n * (-1)):
      ans *= x
    return ans
