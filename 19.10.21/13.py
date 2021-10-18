def convert_base(n, to_base):
    
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


a = (512 ** 78 - 512 ** 60) * (512 ** 5 + 64 ** 5)
print(convert_base(a, 8).count('7'))
