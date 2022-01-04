def f(s):
    s_mas = {}
    for i in range(len(s)-1):
        if s[i] + s[i+1] in s_mas.keys():
            s_mas[s[i] + s[i+1]] += 1
        else:
            s_mas[s[i] + s[i + 1]] = 1
    return s_mas

a = str(input())
b = str(input())
dict_a = f(a)
dict_b = f(b)
cnt = 0
for key in dict_a.keys():
    if key in dict_b.keys():
        cnt += dict_a[key]
print(cnt)
