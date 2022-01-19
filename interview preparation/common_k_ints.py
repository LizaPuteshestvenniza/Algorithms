def indexes(nums, k, ind):
    n = nums[ind]
    ans = [n]
    while k > 1:
        if ((n - nums[ind-1])  < (nums[ind+1] -n)) and (ind-1 >= 0) and (ind+1 < len(nums)):
            ans.append(nums[ind-1])
            k -= 1
        elif ((n - nums[ind-1])  > (nums[ind+1] -n)) and (ind-1 >= 0) and (ind+1 < len(nums)):
            ans.append(nums[ind+1])
            k -= 1
        elif ((n - nums[ind-1])  == (nums[ind+1] -n)) and (ind-1 >= 0) and (ind+1 < len(nums)):
            ans.append(nums[ind+1])
            k -= 1
        elif ind - 1 < 0:
            ans.append(nums[ind+1])
            k -= 1
        elif ind + 1 > len(nums):
            ans.append(nums[ind - 1])
            k -= 1
    return ans
