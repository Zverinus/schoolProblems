nums = [i for i in range(2894, 174882) if str(i)[-1] == '8' and sum(map(int, list(str(i)))) > 22]
print(len(nums), nums[12])
