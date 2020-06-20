def Phi(integer):
    res = integer
    i = 2
    while pow(i, 2) <= integer:
        if integer % i == 0:
            res = res / i * (i - 1)
            while integer % i == 0:
                integer = integer / i

        i += 1
    if integer > 1:
        res = res / integer * (integer - 1)

    return res

x = Phi(24)
print(x)