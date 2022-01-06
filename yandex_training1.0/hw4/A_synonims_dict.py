n = int(input())
dict = {}
for i in range(n):
    pairs = [str(i) for i in input().split()]
    dict[pairs[0]] = pairs[1]
s = str(input())
if s in dict.keys():
    print(dict[s])
else:
    for key,value in dict.items():
        if value == s:
            print(key)
