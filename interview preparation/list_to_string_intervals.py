def intervals(l):
    l = sorted(l)
    if l[0] == l[1] -1:
        ans = str(l[0]) + '-'
    else:
        ans = str(l[0]) + ','
    l.append(-1)
    l.remove(l[0])
    while len(l) > 1:
        if (l[0] == l[1] - 1) and (ans[-1] != '-'):
            ans += str(l[0]) + '-'
            l.remove(l[0])
        elif ans[-1] == '-' and l[0] == l[1] - 1:
            l.remove(l[0])
        elif l[0] != l[1]:
            ans += str(l[0]) + ','
            l.remove(l[0])
    ans = ans[:-1]
    return ans
