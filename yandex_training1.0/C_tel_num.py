new_tel = input()
tel1 = input()
tel2 = input()
tel3 = input()
tel_list = [new_tel, tel1, tel2, tel3]
new_tel_list = []
for i in range(4):
    newt = ''
    for j in range(len(tel_list[i])):
        if tel_list[i][j].isdigit():
            newt += tel_list[i][j]
    if len(newt) == 7:
        newt = '495' + newt
    if len(newt) == 11:
        newt = newt[1:11]
    new_tel_list.append(newt)
for i in range(1, len(new_tel_list)):
    if new_tel_list[0] == new_tel_list[i]:
        print('YES')
    else:
        print('NO')
