file_in = open('input.txt', 'r')
file_out = open('output.txt', 'w')

data = file_in.readlines()
datas = []
for i in data:
    datas.append(i.split())
session = []
dict = {}
for i in range(len(datas)):
    session.append(datas[i][0])
    if datas[i][0] not in dict.keys() :
        dict[datas[i][0]] = datas[i][1:]
    else:
        dict[datas[i][0]] += datas[i][1:]
session = set(session)
cnt = len(session)
closed_session = 0
for val in dict.values():
    if 'CLOSE' not in val:
        closed_session += 1
file_out.write(str(cnt) + '\n')
file_out.write(str(closed_session))
print(dict)
file_in.close()
file_out.close()
