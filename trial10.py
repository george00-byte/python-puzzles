def summation(*args):
    s = 0
    for i in range(len(args)):
        s += args[i]
    return s


print(summation(2, 4))