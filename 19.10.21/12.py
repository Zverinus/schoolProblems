def convert_base(n, to_base):
    
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


a = ((9 * 5 ** 20 + 9) * 5 ** 19 + 9) * 5 ** 18 + 9
b = convert_base(a, 5)
print(b.count('0'), b.count('1'), b.count('2'), b.count('3'), b.count('4'))