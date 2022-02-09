def search(nums, target):
  r = len(nums) -1
  l = -1
  while r > l + 1:
    m = (l + r) // 2
    if nums[m] < target:
      l = m
    else:
      r = m
  if nums[r] != target:
    return -1
  else:
    return r
