a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
first = set(a)
second = set(b)
res = first & second
ans = []
for element in res:
    ans.append(element)
ans = sorted(ans)
r = ''
for i in ans:
    r += str(i) + ' '
print(r)
