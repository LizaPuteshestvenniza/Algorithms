s = [int(i) for i in input().split()]
if len(s) > 1:
    fl = "NO"
    sign = s[0]
    for i in range(1, len(s)):
        if sign < s[i]:
            fl = "YES"
            sign = s[i]
        elif sign >= s[i]:
            fl = "NO"
            break
    print(fl)
else:
    print('YES')
