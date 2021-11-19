def lengthOfLastWord(s):
    arr = s.split()
    max = -1
    for i in arr:
        if i.isalpha():
            if (len(i)) > max:
                max = len(i)
        else:
            continue
    return max
