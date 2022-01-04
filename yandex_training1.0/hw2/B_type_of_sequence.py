def find(a):
    sign = a[0]
    for i in range(1, len(a)):
        if sign == a[i]:
            sign = a[i]
        else:
            break
        if i == len(a) - 1:
            return 'CONSTANT'
    sign = a[0]
    for i in range(1, len(a)):
        if sign < a[i]:
            sign = a[i]
        else:
            break
        if i == len(a) - 1:
            return 'ASCENDING'
    sign = a[0]
    for i in range(1, len(a)):
        if sign <= a[i]:
            sign = a[i]
        else:
            break
        if i == len(a) - 1:
            return 'WEAKLY ASCENDING'
    sign = a[0]
    for i in range(1, len(a)):
        if sign > a[i]:
            sign = a[i]
        else:
            break
        if i == len(a) - 1:
            return 'DESCENDING'
    sign = a[0]
    for i in range(1, len(a)):
        if sign >= a[i]:
            sign = a[i]
        else:
            break
        if i == len(a) - 1:
            return 'WEAKLY DESCENDING'
    return 'RANDOM'

res = []
i = int(input())
while i != -2000000000:
    res.append(int(i))
    i = int(input())

print(find(res))
