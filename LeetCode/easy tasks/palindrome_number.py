class Solution(object):
    def isPalindrome(self, x):
        res = str(x)
        res1 = res[::-1]
        return res == res1
