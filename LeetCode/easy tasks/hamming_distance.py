def hammingDistance(x, y):
    def turn(x):
        res = ''
        while x > 1:
            ost = int(x % 2)
            res += str(ost)
            x = x / 2
        if x == 1:
            ost = '1'
            res += ost
        res = res[::-1]
        return(list(res))
    res_x = turn(x)
    res_y = turn(y)
    if len(res_x) < len(res_y):
        while len(res_x) != len(res_y):
            res_x.insert(0, '0')
    elif len(res_y) < len(res_x):
        while len(res_x) != len(res_y):
            res_y.insert(0, '0')
    s = 0
    for i in range(len(res_x)):
        if res_x[i] != res_y[i]:
            s += 1
    return s
