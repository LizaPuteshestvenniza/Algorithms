a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if (d == 0) or (e == 0):
    print('NO')
elif ((a*b) <= (d*e)) and (((a<=d) and (b<=e)) or ((a<=e) and (b<=d))) :
    print('YES')
elif ((b*c) <= (d*e)) and (((c<=d) and (b<=e)) or ((c<=e) and (b<=d))):
    print('YES')
elif ((a*c) <= (d*e)) and (((a<=d) and (c<=e)) or ((a<=e) and (c<=d))) :
    print('YES')
else:
    print('NO')
