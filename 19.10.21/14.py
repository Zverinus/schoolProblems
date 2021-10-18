def convert_base(n, to_base):
    
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


a = 2435
for i in range(2, 11):
    print(sum(map(int, list(convert_base(a, i)))), i)
