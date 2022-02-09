def sortedSquares(nums):
  for i in range(len(nums)):
    nums[i] *= nums[i]
  return sorted(nums)
