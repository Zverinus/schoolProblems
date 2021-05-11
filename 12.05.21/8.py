for num in range(35612, 57355):
    divisors = []
    for divisor in range(2, num // 2 + 1):
        if num % divisor == 0:
            divisors.append(divisor)
            if len(divisors) > 6:
                break
    if len(divisors) == 6:
        print(f'{num}: {" ".join(map(str, sorted(divisors)))}')
