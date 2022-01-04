def f(set_i):
    mas = []
    for el in set_i:
        mas.append(el)
    mas = sorted(mas)
    res = ''
    for element in mas:
        res += str(element) + ' '
    print(len(mas))
    print(res)

num = [int(i) for i in input().split()]
ann = [0 for i in range(num[0])]
for i in range(num[0]):
    ann[i] = int(input())
borya = [0 for i in range(num[1])]
for i in range(num[1]):
    borya[i] = int(input())
ann = set(ann)
borya = set(borya)
f(ann & borya)
f(ann - borya)
f(borya - ann)
