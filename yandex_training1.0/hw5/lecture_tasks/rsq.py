def prefsum(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1,len(prefixsum)):
        prefixsum[i] = prefixsum[i-1] + nums[i-1]
    return prefixsum

def sum_cnt(prefixsum, L, R):
    return prefixsum[R] - prefixsum[L]

nums = [int(i) for i in input().split()]
boarders = [int(i) for i in input().split()]
print(sum_cnt(prefsum(nums),boarders[0],boarders[1]))
