# Наивное решение 315/318 тестов
def threeSum(self, nums):
    ans = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(i,j):
                if i != j and i != k and j != k and (nums[i] + nums[j] + nums[k]) == 0:
                    tmp = [nums[i], nums[j], nums[k]]
                    tmp = sorted(tmp)
                    if tmp not in ans:
                        ans.append(tmp)
        return ans

# Решение со словарем 243/318 тестов
def threeSum(nums):
    dict = {}
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            tmp = (i, j,)
            if tmp not in dict.keys() and i != j:
                dict[tmp] = nums[i] + nums[j]
    ans = []
    for k in range(len(nums)):
        for key, val in dict.items():
            key2 = list(key)
            if nums[k] + val == 0 and k not in key2:
                ans_tmp = [nums[key2[0]], nums[key2[1]], nums[k]]
                ans_tmp = sorted(ans_tmp)
                if ans_tmp not in ans:
                    ans.append(ans_tmp)
    return ans
