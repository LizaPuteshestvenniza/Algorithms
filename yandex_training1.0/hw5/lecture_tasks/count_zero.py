def presum(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(prefixsum)):
        if nums[i-1] == 0:
            prefixsum[i] = prefixsum[i-1] + 1
        else:
            prefixsum[i] = prefixsum[i - 1]
    return prefixsum

def count_zero(preixsum, L, R):
    return preixsum[R] - preixsum[L]

nums = [int(i) for i in input().split()]
m = int(input())
for i in range(m):
    boarders = [int(i) for i in input().split()]
    print(count_zero(presum(nums), boarders[0], boarders[1]))
