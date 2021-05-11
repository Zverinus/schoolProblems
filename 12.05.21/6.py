for i in range(10000):
    x = i
    a = 0
    b = 0
    while x > 0:
        a = a + 2
        b = b + (x % 10)
        x = x // 10
    if a == 6 and b == 5:
        print(i)
        break
# 104
