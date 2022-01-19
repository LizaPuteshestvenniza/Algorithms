def rle(s):
    s += ' '
    counter = 0
    ans = s[0]
    while s[0] != ' ':
        if s[0] == ans[-1]:
            counter += 1
            s = s[1:]
        else:
            ans += str(counter)
            ans += s[0]
            counter = 0
    ans += str(counter)
    return ans

def back_rle(s):
    ans = ''
    while len(s) > 0:
        for i in range(int(s[1])):
            ans += s[0]
        s = s[2:]
    return ans
