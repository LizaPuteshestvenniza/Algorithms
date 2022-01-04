a = [int(i) for i in input().split()]
s = str(input())
mas = []
for i in range(len(s)):
    mas.append(int(s[i]))
a = set(a)
mas = set(mas)
res = mas - a
print(len(res))
