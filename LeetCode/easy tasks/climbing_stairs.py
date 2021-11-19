def climbStairs(self, n):
    arr = [0] * n
    arr[0] = 1
    if n > 1:
        arr[1] = 1
    for i in range(n):
        if (i+1) < len(arr):
            arr[i+1] += arr[i]
        if (i+2) < len(arr):
            arr[i+2] += arr[i]
    return arr[-1]
