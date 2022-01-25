def myAtoi(s):
    if len(s) > 0:
        ans = ''
        for i in range(len(s)):
            if s[i].isspace() and ans == '':
                continue
            elif s[i] == '-':
                if ans == '':
                    ans = '-'
                else:
                    break
            elif s[i] == '+':
                if ans == '':
                    ans = '+'
                else:
                    break
            elif s[i].isdigit():
                ans += s[i]
            elif s[i].isspace() and ans != '':
                break
            elif s[i].isalpha() or s[i] == '.' or s[i] == ',':
                break
        if ans == '' or ans == '-' or ans == '+':
            return 0
        elif int(ans) < -2147483648:
            return -2147483648
        elif int(ans) > 2147483647:
            return 2147483647
        return int(ans)
    else:
        return 0
