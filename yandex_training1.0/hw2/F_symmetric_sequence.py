def f(a):
    if a == a[::-1]:
        return 0
    else:
        cnt = 0
        res = []
        for i in range(len(a)):
            if a[i] != a[(-i)+1] or a != a[::-1]:
                a.insert(len(a)-i, a[i])
                cnt += 1
                res.insert(0, a[i])
            if a == a[::-1]:
                break
        return cnt, res

n = int(input())
r = [int(i) for i in input().split()]
if r == r[::-1]:
    print(0)
else:
    ans = f(r)
    print(ans[0])
    ansn = ''
    for i in ans[1]:
        ansn += str(i) + ' '
    print(ansn)
