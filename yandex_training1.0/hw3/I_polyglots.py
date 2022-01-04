def f(n_s):
    mas = []
    for el in n_s:
        mas.append(str(el))
    for i in mas:
        print(i)

n = int(input())
m = int(input())
languages = [' ' for i in range(m)]
for i in range(m):
    languages[i] = str(input())
languages = set(languages)
res = set(languages)
ans = set(languages)
for i in range(1,n):
    new_m = int(input())
    new_languages = [' ' for j in range(new_m)]
    for j in range(new_m):
        new_languages[j] = str(input())
    new_languages = set(new_languages)
    ans = new_languages | ans
    res = new_languages & res
print(len(res))
f(res)
print(len(ans))
f(ans)
