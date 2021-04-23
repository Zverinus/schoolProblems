suitable_nums = [i for i in range(1170, 8368) if (i % 3 == 0 or i % 7 == 0)
                 and i % 11 != 0 and i % 13 != 0 and i % 17 != 0 and i % 19 != 0]
print(f"Кол-во: {len(suitable_nums)}, миниамльное:{min(suitable_nums)}")
