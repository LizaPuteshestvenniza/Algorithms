def football(nums):
    max_prof = 0
    tmp = 0
    j = 0
    for i in range(len(nums)):
        while j < len(nums) and (nums[i] + nums[i+1] >= nums[j] or i==j):
            tmp += nums[j]
            j += 1
        if max_prof < tmp:
            max_prof = tmp
        tmp -= nums[i]
        if j == len(nums) - 1:
            break
    return max_prof
