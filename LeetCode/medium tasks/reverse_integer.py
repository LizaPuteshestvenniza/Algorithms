def reverse(self, x):
    s = str(x)
    s = s[::-1]
    if s[0] == 0:
        s = s[1:]
    if s[-1] == '-':
        s = '-' + s[:-1]
    if int(s) < -2147483648 or int(s) > 2147483647:
        return 0
    return int(s)
