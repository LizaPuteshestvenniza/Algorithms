a = [int(i) for i in input().split()]
n = a[0]
m = a[1]
mins = a[2]
res = [[0] * (m+2) for i in range(n+2)]
for i in range(mins):
    mina = [int(i) for i in input().split()]
    a1 = mina[0]
    b1 = mina[1]
    res[a1][b1] = '*'
di = [1,1,1,0,0,-1,-1,-1]
dj = [-1,0,1,-1,1,-1,0,1]
for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(len(di)):
            if res[i][j] == '*':
                if res[i+di[k]][j+dj[k]] != '*':
                    res[i+di[k]][j+dj[k]] += 1

for i in range(1,n+1):
    for j in range(1,m+1):
        print(res[i][j], end=' ')
    print('')
