def main():
    nums = [int(input("Введите число: ")) for i in range(int(input("Введите количество чисел: ")))]
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    print(f"Минимальное число: {nums[0]}")
    print(f"Максимальное число: {nums[-1]}")


if __name__ == '__main__':
    main()
