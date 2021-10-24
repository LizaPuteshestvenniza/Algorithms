def merge(a, b):
    i = 0
    j = 0
    c = []
    while(i < len(a)) or (j < len(b)):
        if (j == len(b)) or ((i < len(a)) and (a[i]) < b[j]) :
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return c

def mergeSort(a):
    n = len(a)
    if n <= 1:
        return a
    if (n % 2 != 0):
        m = int((n-1) / 2)
    else:
        m = int(n / 2)
    l = []
    for i in range(0, m):
        l.append(a[i])
    r = []
    for i in range(m, n) :
        r.append(a[i])
    l = mergeSort(l)
    r = mergeSort(r)
    return(merge(l, r))

n = int(input())
my_list = [int(el) for el in input().split()]
new_list = mergeSort(my_list)
for i in range(0, n):
    print(new_list[i], end = ' ')
