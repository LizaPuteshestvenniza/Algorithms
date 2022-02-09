def firstBadVersion(n):
  r = n 
  l = -1
  while r > l + 1:
    m = (l + r) // 2
    if isBadVersion(m) == False:
      l = m
    else:
      r = m
  return r
