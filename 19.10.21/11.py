def convert_base(n, to_base):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


a = 16 ** 20 + 2 ** 30 - 32

print(convert_base(a, 4).count('3'))