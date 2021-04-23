suitable_nums = [i for i in range(-7018, 3791) if i % 6 == 0 and i % 7 != 0 and i % 19 != 0 and str(i)[-1] != 2]
print(f"Кол-во: {len(suitable_nums)}, минимальное:{min(suitable_nums)}")
