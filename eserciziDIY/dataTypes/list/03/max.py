numeri = input("inserisci dei numeri\n")

def mas(numeri):
    numeri = [int(x) for x in numeri.split(',')]
    # list comprehension: [espressione for variabile in sequenza if condizione]
    mas = max(numeri)
    return mas
print(mas(numeri))