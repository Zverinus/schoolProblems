array = [int(input()) for i in range(20)]
for i in range(1, len(array) - 1, 2):
    array[i], array[i + 1] = array[i + 1], array[i]
print(*array)
