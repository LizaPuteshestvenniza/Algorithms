def time(n, tin, tout, boss):
    event = []
    for i in range(len(tin)):
        event.append([tin[i], -1])
        event.append([tout[i], 1])
    for i in range(len(boss)):
        event.append(([boss[i], 0]))
    event = sorted(event)
    online = 0
    boss_list = []
    for i in range(len(event)):
        if event[i][1] == -1:
            online += 1
        elif event[i][1] == 1:
            online -= 1
        elif  event[i][1] == 0:
            boss_list.append(online)
    return boss_list

n = int(input())
tin = [int(i) for i in input().split()]
tout = [int(i) for i in input().split()]
boss = [int(i) for i in input().split()]
print(time(n, tin, tout, boss))
