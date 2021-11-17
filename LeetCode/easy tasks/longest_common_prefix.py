class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ''
        min = strs[0]
        for i in (strs):
            if len(i) < len(min) :
                min = i
        for i in range(len(min)):
            for j in range(len(strs)):
                if strs[j][i] == min[i]:
                    if j == len(strs)-1:
                        res += min[i]
                    continue
                else:
                    break
            if len(res) != i+1:
                break
        return(res)
