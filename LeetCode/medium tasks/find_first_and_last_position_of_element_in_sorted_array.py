def searchRange(self, nums, target):
  if target in nums:
    ans = []
    while target in nums:
      tmp = nums.index(target) 
      ans.append(tmp)
      nums.insert(tmp, -1)
      nums.remove(target)
    return [ans[0], ans[-1]]
  else:
    return [-1,-1]
