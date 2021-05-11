for i in range(10000):
    x = i
    L = 0
    M = 0
    while x > 0:
        L = L + 1
        if M < x:
            M = x % 10
        x = x // 10
    if L == 3 and M == 7:
        print(i)
        break
# 170
