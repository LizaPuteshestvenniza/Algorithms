class Solution(object):
    def romanToInt(self, s):
        s = ' ' + s + ' '
        res = 0
        for i in range(len(s)):
            if s[i] == 'I' and ((s[i+1] != 'V') and (s[i+1] != 'X')):
                res +=1
            if s[i] == 'I' and s[i + 1] == 'V':
                res += 4
            if s[i] == 'V' and s[i-1] != 'I':
                res += 5
            if s[i] == 'I' and s[i + 1] == 'X':
                res += 9
            if s[i] == 'X' and ((s[i + 1] != 'L') and (s[i-1] != 'I') and (s[i + 1] != 'C')):
                res += 10
            if s[i] == 'X' and s[i + 1] == 'L':
                res += 40
            if s[i] == 'L' and s[i-1] != 'X':
                res += 50
            if s[i] == 'X' and s[i + 1] == 'C':
                res += 90
            if s[i] == 'C' and ((s[i + 1] != 'D') and (s[i-1] != 'X') and (s[i + 1] != 'M')):
                res += 100
            if s[i] == 'C' and s[i + 1] == 'D':
                res += 400
            if s[i] == 'D' and s[i-1] != 'C':
                res += 500
            if s[i] == 'C' and s[i + 1] == 'M':
                res += 900
            if s[i] == 'M' and s[i-1] != 'C':
                res += 1000
        return res
        
