parola = input("scrivi una parola\n")


def count(parola):
    lettere = []
    numeri = []
    for x in parola:
        if x.isalpha():
            lettere.append(x)
        elif x.isdigit():
            numeri.append(x)
    num, let = len(numeri), len(lettere)
    return f"numeri: {num} lettere: {let}"
print(count(parola))