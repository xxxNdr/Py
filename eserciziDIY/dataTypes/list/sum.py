lista = input("inserisci una lista di elementi separati da virgola\n")


def somma(lista):
    lista = list(lista.split(","))
    print()
    for x in lista:
        print(x)
    return len(lista)

print("la lunghezza della tua lista è: ", somma(lista))
