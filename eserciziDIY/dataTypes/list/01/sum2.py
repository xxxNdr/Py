numeri = input("inserisci dei numeri\n")

def somma(numeri):
    return sum(map(int, numeri.split(',')))
print(somma(numeri))
