def f(a):
    cnt = 0
    for i in range(1,len(a)-1):
        if a[i] > a[i-1] and a[i] > a[i+1]:
            cnt += 1
    return cnt

arr = [int(i) for i in input().split()]
print(f(arr))
