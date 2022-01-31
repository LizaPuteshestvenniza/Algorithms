def bin_search(a,b,n):
    l = 0
    r = n * (a+b)
    while r > l + 1:
        m = (l + r) // 2
        if (m // a) * (m // b) >= n:
            r = m
        else:
            l = m
    print(r)

arr = [int(i) for i in input().split()]
w = arr[0]
h = arr[1]
n = arr[2]
bin_search(w,h,n)
