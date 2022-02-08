# 775/992 тестов

def divide(dividend, divisor):
    def minus_(x):
        if x < 0:
            x -= x + x
        return x

    if dividend == 0:
        return 0
    if dividend == divisor:
        return 1
    flag = 1
    if (divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0):
        flag = -1
    if (divisor < 0 and dividend < 0):
        flag = 0
    divisor = minus_(divisor)
    dividend = minus_(dividend)
    if divisor == 1:
        if flag == 1:
            return dividend
        if flag == 0:
            return dividend - 1
        if flag == -1:
            return dividend * (-1)
    if dividend < divisor:
        return 0
    ans = 1
    prev_div = divisor
    while divisor + prev_div < dividend:
        divisor += divisor
        ans += 1
    if flag == 0:
        return ans - 1
    return ans * flag
