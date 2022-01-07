import sys
x = sys.stdin.read()
text = x.split('\n')
for i in range(len(text)):
    text[i] = text[i].split()
grand_text = []
for i in range(len(text)):
    for j in range(len(text[i])):
        grand_text.append(text[i][j])
dict = {}
for i in range(len(grand_text)):
    if grand_text[i] in dict.keys():
        dict[grand_text[i]] += 1
    else:
        dict[grand_text[i]] = 0
    print(dict[grand_text[i]], end=' ')
