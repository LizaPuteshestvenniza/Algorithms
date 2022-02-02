def time(n, tin, tout):
    event = []
    for i in range(len(tin)):
        event.append([tin[i], -1])
        event.append([tout[i], 1])
    event = sorted(event)
    max_time = 0
    online = 0
    for i in range(len(event)):
        if online > 0:
            max_time += event[i][0] - event[i-1][0]
        if event[i][1] == -1:
            online += 1
        else:
            online -= 1
    return max_time

n = int(input())
tin = [int(i) for i in input().split()]
tout = [int(i) for i in input().split()]
print(time(n, tin, tout))
