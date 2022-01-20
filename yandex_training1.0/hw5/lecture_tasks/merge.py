def merge(nums1, nums2):
    ans = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            ans.append(nums1[i])
            i += 1
        else:
            ans.append(nums2[j])
            j += 1
    if i == len(nums1):
        ans += nums2[j:]
    if j == len(nums2):
        ans += nums1[i:]
    return ans
