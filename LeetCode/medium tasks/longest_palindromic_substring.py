# наивное решение:
def longestPalindrome(s):
    ans = ''
    cnt = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            tmp = ''
            for k in range(i, j):
                tmp += s[k]
            if (len(tmp) > cnt) and (tmp == tmp[::-1]):
                ans = tmp
                cnt = len(tmp)
    return ans
  
  
