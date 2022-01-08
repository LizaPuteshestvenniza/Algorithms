def balance(l):
    if l[1] in dict.keys():
        return(str(dict[l[1]]) + '\n')
    else:
        return('ERROR' + '\n')
def income(l):
    for key,val in dict.items():
        if val > 0:
            dict[key] = int(val * ((int(l[1]) / 100) + 1))
def deposit(l):
    if l[1] in dict.keys():
        dict[l[1]] += int(l[2])
    else:
        dict[l[1]] = int(l[2])
def withdraw(l):
    if l[1] in dict.keys():
        dict[l[1]] -= int(l[2])
    else:
        dict[l[1]] = int(l[2]) * (-1)
def transfer(l):
    if l[1] in dict.keys():
        dict[l[1]] -= int(l[3])
    else:
        dict[l[1]] = int(l[3]) * (-1)
    if l[2] in dict.keys():
        dict[l[2]] += int(l[3])
    else:
        dict[l[2]] = int(l[3])



file_in = open('input.txt', 'r')
file_out = open('output.txt', 'w')
data = file_in.readlines()
for i in range(len(data)):
    data[i] = data[i].split()
dict = {}
for i in range(len(data)):
    if 'DEPOSIT' in data[i]:
        deposit(data[i])
    if 'WITHDRAW' in data[i]:
        withdraw(data[i])
    if 'BALANCE' in data[i]:
        file_out.write(balance(data[i]))
    if 'TRANSFER' in data[i]:
        transfer(data[i])
    if 'INCOME' in data[i]:
        income(data[i])
