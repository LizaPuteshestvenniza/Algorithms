size = [int(i) for i in input().split()]
a1 = size[0]
b1 = size[1]
a2 = size[2]
b2 = size[3]

res = []

if b1 > b2:
    res.append(b1*(a1+a2))
else:
    res.append(b2 * (a1 + a2))
if a1 > a2:
    res.append(a1 * (b1 + b2))
else:
    res.append(a2 * (b1 + b2))
if a1 > b2:
    res.append(a1 * (b1 + a2))
else:
    res.append(b2 * (b1 + a2))
if b1 > a2:
    res.append(b1 * (a1 + b2))
else:
    res.append(a2 * (a1 + b2))

s = res.index(min(res))
if s == 0:
    print(int(res[0] / (a1 + a2)), a1 + a2)
elif s == 1:
    print(int(res[1] / (b1 + b2)), b1 + b2)
elif s == 2:
    print(int(res[2] / (b1 + a2)), b1 + a2)
elif s == 3:
    print(int(res[3] / (a1 + b2)), a1 + b2)
