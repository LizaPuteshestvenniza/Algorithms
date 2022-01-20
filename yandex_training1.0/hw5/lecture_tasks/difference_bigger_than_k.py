# Решение за O(n^2)
nums = [int(i) for i in input().split()]
k = int(input())
cnt = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[j] - nums[i] > k:
            cnt += 1

print(cnt)

# Решение за O(n):
nums = [int(i) for i in input().split()]
k = int(input())
cnt = 0
j = 0
for i in range(len(nums)):
    while j < len(nums) and nums[j] - nums[i] <= k:
        j += 1
    if nums[j] - nums[i] > k:
        cnt += len(nums) - j
    if j == len(nums) - 1:
        break
print(cnt)
