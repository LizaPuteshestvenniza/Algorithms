a = [int(i) for i in input().split()]
if len(a) == 3:
    a1 = a[0]
    b1 = a[1]
    c1 = a[2]
    print(a1,b1,c1)
else:
    a_cop = a
    min1 = min(a)
    a.remove(min1)
    min2 = min(a)

    max1 = max(a_cop)
    a_cop.remove(max1)
    max2 = max(a_cop)
    a_cop.remove(max2)
    max3 = max(a_cop)
    if max1 * max2 * max3 > max1 * min1 * min2:
        print(max1, max2, max3)
    else:
        print(max1, min1, min2)
