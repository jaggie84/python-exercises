def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([11, 22, 33, 44, 55, 66, 77, 88, 99]))