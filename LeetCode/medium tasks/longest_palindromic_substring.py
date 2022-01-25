# наивное решение за O(n^3):
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

# решение за O(n^2): 167/180 тестов
def longestPalindrome(s):
    ans = ''
    cnt = 0
    for i in range(len(s)):
        tmp = ''
        for j in range(i, len(s)):
            tmp += s[j]
            if (len(tmp) > cnt) and (tmp == tmp[::-1]):
                ans = tmp
                cnt = len(tmp)
    return ans
  
  
