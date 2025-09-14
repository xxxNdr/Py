lista = [1, 2, [3, 4], 5, [6]]


def s(l: list):
    total = 0
    latot = 0
    for x in l:
        if type(x) == type(1):
            total += x
        elif type(x) == type([]):
            latot += s(x)
    return total + latot


print(s(lista))
