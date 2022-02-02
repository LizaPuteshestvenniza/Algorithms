def events(n, tin, tout):
    event = []
    for i in range(len(tin)):
        event.append([tin[i], 1])
        event.append(([tout[i], -1]))
    event = sorted(event)
    online = 0
    max_online = 0
    for i in range(len(event)):
        if event[i][1] == 1:
            online += 1
        if event[i][1] == -1:
            online -= 1
        max_online = max(max_online, online)
    return max_online

n = int(input())
tin = [int(i) for i in input().split()]
tout = [int(i) for i in input().split()]
print(events(n, tin, tout))
