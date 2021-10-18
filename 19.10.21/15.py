def convert_base(n, to_base):

    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


a = 7 ** 2 + 49 ** 4 - 21
print(convert_base(a, 14).count('A'))
