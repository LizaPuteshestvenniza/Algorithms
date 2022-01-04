n = int(input())
field = []
for i in range(n):
    coordinats = [int(i) for i in input().split()]
    field.append(coordinats[0])
print(len(set(field)))
