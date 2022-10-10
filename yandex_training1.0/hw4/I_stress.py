n = int(input())
dicti = {}

for i in range(n):
    t = str(input())
    if t.lower() in dicti.keys():
        dicti[t.lower()].append(t)
    else:
        dicti[t.lower()] = [t]

inp = str(input())
ans = 0
for i in inp.split():
    cnt = 0
    for j in i:
        if j.isupper():
            cnt += 1
    if cnt > 1 or cnt == 0:
        ans +=1
    elif i.lower() in dicti.keys():
        if i not in dicti[i.lower()]:
            ans += 1

print(ans)
