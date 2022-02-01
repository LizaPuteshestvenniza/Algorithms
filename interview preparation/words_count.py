s = str(input())
s = s.split()
dict = {}
for i in s:
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1

sorted_val = sorted(dict.values())
sorted_val = sorted_val[::-1]
sorted_dict = {}
for i in sorted_val:
    for key, val in dict.items():
        if i == val:
            sorted_dict[key] = i
ans = list(sorted_dict.keys())
for i in range(5):
    print(ans[i])
