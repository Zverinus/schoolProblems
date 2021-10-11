words = [input() for i in range(20)]
print(" ".join(filter(lambda x: len(x) == 4 and "щ" in x, words)))
print(" ".join(filter(lambda x: x[0] == x[-1], words)))
