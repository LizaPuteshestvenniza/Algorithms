temp = [int(i) for i in input().split()]
reg = input()
if reg == 'freeze':
    if temp[0] < temp[1]:
        print(temp[0])
    else:
        print(temp[1])
if reg == 'heat':
    if temp[0] > temp[1]:
        print(temp[0])
    else:
        print(temp[1])
if reg == 'auto':
    print(temp[1])
if reg == 'fan':
    print(temp[0])
