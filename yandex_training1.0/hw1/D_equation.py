if a == 0:
    if (c**2 == b):
        print('MANY SOLUTIONS')
    else:
        print('NO SOLUTION')
else:
    if c < 0:
        print('NO SOLUTION')
    else:
        x = (c**2 - b) / a
        f = (a * x + b)
        if f == (c ** 2):
            if (x - int(x)) == 0:
                print(int(x))
            else:
                print('NO SOLUTION')
