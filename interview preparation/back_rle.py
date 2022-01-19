def back_rle(s):
    ans = ''
    while len(s) > 0:
        for i in range(int(s[1])):
            ans += s[0]
        s = s[2:]
    return ans
