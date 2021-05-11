k = 0
for i in range(10000):
    s = i
    n = 10
    while s > 0:
        s = s - 15
        n = n + 3
    if n == 31:
        k += 1
print(k)
# 15
