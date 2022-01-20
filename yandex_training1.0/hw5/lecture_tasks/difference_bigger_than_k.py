# Решение за O(n^2)
nums = [int(i) for i in input().split()]
k = int(input())
cnt = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[j] - nums[i] > k:
            cnt += 1

print(cnt)
