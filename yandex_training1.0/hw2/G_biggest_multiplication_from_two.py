max = 0
max2 = 0
a = [int(i) for i in input().split()]


if a[0] > a[1]:
    max = a[0]
    max2 = a[1]
else:
    max = a[1]
    max2 = a[0]

min = 0
min2 = 0

if a[0] < a[1]:
    min = a[0]
    min2 = a[1]
else:
    min = a[1]
    min2 = a[0]


for i in range(2, len(a)):
    if a[i] > max:
        max2 = max
        max = a[i]
    elif a[i] > max2 and a[i] <= max:
        max2 = a[i]
for i in range(2, len(a)):
    if a[i] < min:
        min2 = min
        min = a[i]
    elif a[i] < min2 and a[i] >= min:
        min2 = a[i]

if max * max2 > min * min2:

    print(max2, max)
else:
    print(min, min2)
