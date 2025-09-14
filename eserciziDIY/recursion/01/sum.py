lista = [1,13,255,1000]

def su(x: list):
    if len(x) == 1:
        return x[0]
    else:
        return x[0] + su(x[1:])
    
print(su(lista))