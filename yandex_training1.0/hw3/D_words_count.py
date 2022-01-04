import sys
x = sys.stdin.read()
text = x.split('\n')
for i in range(len(text)):
    text[i] = text[i].split()
grand_text = []
for i in range(len(text)):
    for j in range(len(text[i])):
        grand_text.append(text[i][j])
print(len(set(grand_text)))
