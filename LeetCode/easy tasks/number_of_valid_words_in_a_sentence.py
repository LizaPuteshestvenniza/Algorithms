def countValidWords(sentence):
    s = sentence.split()
    cnt = 0
    t = 0
    a = s[0]
    b = s[-1]
    if a[0] == '"' and b[-1] == '"':
        a = a[1:]
        b = b[0:len(s[-1]) - 1]
        s[0] = a
        s[-1] = b
    for i in s:
        if i.isdigit():
            continue
        else:
            for j in range(len(i)):
                if j == 0 and i[j] == '-':
                    break
                if (j != len(i) - 1) :
                    if (i[j].islower() and i[j].isalpha()):
                        continue
                    elif not ((i[j].islower() and i[j].isalpha()) or (i[j] == '-' and t == 0)):
                        break
                    if (i[j] == '-' and (i[j-1].isalpha() and i[j+1].isalpha() and t == 0)):
                        t += 1
                    if (i[j] == '-') and (not (i[j-1].isalpha() and i[j+1].isalpha())):
                        break
                if (j == len(i) - 1) and ((i[j] == '!') or (i[j] == ',') or (i[j] == '.') or (i[j].isalpha() and i[j].islower())):
                    cnt +=1
            t = 0
    return cnt
