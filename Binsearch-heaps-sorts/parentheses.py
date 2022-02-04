def f(s):
    a = []
    for i in s:
        if i == '(':
            a.append('(')
        else:
            if len(a) == 0:
                return 0
            else:
                a.pop()
    if len(a) == 0:
        return 1
    else:
        return 0


s = str(input())
print(f(s))
