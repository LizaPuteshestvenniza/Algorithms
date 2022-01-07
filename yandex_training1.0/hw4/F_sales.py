file_in = open('input.txt', 'r')
file_out = open('output.txt', 'w')
data = file_in.readlines()
dict = {}
for i in range(len(data)):
    data[i] = data[i].split()
    if data[i][0] not in dict.keys():
        dict[data[i][0]] = {}
        dict[data[i][0]][data[i][1]] = int(data[i][2])
    else:
        if data[i][1] in dict[data[i][0]].keys():
            dict[data[i][0]][data[i][1]] += int(data[i][2])
        else:
            dict[data[i][0]][data[i][1]] = int(data[i][2])
for key in sorted(dict.keys()):
    file_out.write(key + ':' + '\n')
    for key2 in sorted(dict[key].keys()):
        file_out.write(key2 + ' ' + str(dict[key][key2]) + '\n')

file_in.close()
file_out.close()
