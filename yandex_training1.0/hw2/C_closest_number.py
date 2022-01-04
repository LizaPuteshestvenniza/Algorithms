def fin(a):
    a = sorted(a)
    if goal < a[0]:
        return a[0]
    elif goal > a[-1]:
        return a[-1]
    else:
        tmp = []
        for i in range(len(a)):
            tmp.append(abs(goal - a[i]))
        ind = tmp.index(min(tmp))
        return a[ind]

n = int(input())
arr = [int(i) for i in input().split()]
goal = int(input())

print(fin(arr))
