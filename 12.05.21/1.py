eight_counter = 0
for num in range(1, 1000):
    r = num
    r = num // 3 if num % 3 else num - 1
    r = r // 5 if r % 5 == 0 else r - 1
    r = r // 11 if r % 11 == 0 else r - 1
    if r == 8:
        eight_counter += 1
print(eight_counter)