n = int(input())
dict = {}
for i in range(n):
    block = [int(i) for i in input().split()]
    if block[0] not in dict.keys():
        dict[block[0]] = block[1]
    else:
        if dict[block[0]] < block[1]:
            dict[block[0]] = block[1]
sum = 0
for val in dict.values():
    sum += val
print(sum)
