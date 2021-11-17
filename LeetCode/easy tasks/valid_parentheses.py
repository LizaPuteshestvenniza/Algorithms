class Solution(object):
    def isValid(self, s):
        while (len(s) != 0) and (len(s) % 2 == 0) and (('(' in s and ')' in s) or ('[' in s and ']' in s) or ('{' in s and '}' in s)):
            size = len(s)
            if (size == 2) and ((s[0] == ')' and s[1] == '(') or (s[0] == ']' and s[1] == '[') or (s[0] == '}' and s[1] == '{')):
                return False
            for i in range(len(s)):
                if ((s[i] == '(' and s[i+1] == ')') or (s[i] == '[' and s[i+1] == ']') or (s[i] == '{' and s[i+1] == '}')) and size >= 2:
                    s = s[0:i] + s[i+2:size]
                    break
                if ((s[i] == '(' and (s[i+1] == ']' or s[i+1] == '}')) or (s[i] == '[' and (s[i+1] == ')' or s[i+1] == '}')) or (s[i] == '{' and (s[i+1] == ']' or s[i+1] == ')'))) and size >= 2:
                    return False
        if s == '':
            return True
        else:
            return False
