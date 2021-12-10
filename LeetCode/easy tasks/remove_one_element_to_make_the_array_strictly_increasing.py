def canBeIncreasing(nums):
    cnt = 0
    tmp = 0
    if len(nums) == 2:
        return True
    while len(nums) > 1:
        if nums[0] < nums[1]:
            tmp = nums[0]
            nums.remove(nums[0])
        else:
            if cnt == 0:
                cnt += 1
                if len(nums) == 2:
                    return True
                else:
                    if tmp < nums[0] and nums[0] < nums[2] :
                        nums.remove(nums[1])
                    elif tmp < nums[1]:
                        nums.remove(nums[0])
            else:
                return False
    if len(nums) == 1:
        return True
