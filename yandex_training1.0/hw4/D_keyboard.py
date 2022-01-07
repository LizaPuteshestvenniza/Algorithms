n = int(input())
keyboard = [int(i) for i in input().split()]
k = int(input())
seq = [int(i) for i in input().split()]
dict = {}
for i in range(len(seq)):
    if seq[i] in dict.keys():
        dict[seq[i]] += 1
    else:
        dict[seq[i]] = 1
keyboard.insert(0, 0)
for i in range(1,len(keyboard)):
    if dict[i] <= keyboard[i]:
        print('NO')
    else:
        print('YES')
