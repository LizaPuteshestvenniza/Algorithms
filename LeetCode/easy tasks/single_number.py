def singleNumber(nums):
    d = {}
    for i in nums:
        if i in list(d.keys()):
            d[i] += 1
        else:
            d[i] = 1
    for key, value in d.items():
        if value == 1:
            return key
