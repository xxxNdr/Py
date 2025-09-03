
numeri = input("inserisci dei numeri\n")

def somma(numeri):
    somma = 0
    for x in numeri.split(','):
        somma += int(x)
    return somma
print(somma(numeri))