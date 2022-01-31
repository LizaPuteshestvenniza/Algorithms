def bin_search(x):
    l = -1
    r = len(seq) - 1
    while r > l + 1:
        m = (l + r) // 2
        if seq[m] < x:
            l = m
        else:
            r = m
    if seq[r] != x:
        return 'NO'
    else:
        return 'YES'

nk = [int(i) for i in input().split()]
n = nk[0]
k = nk[1]
seq = [int(i) for i in input().split()]
xes = [int(i) for i in input().split()]
for i in xes:
    print(bin_search(i))
