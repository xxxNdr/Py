parole = []

while True:
    parola = input("inserisci una parola o una frase")
    # è molto importante che l'imput sia dentro il ciclo
    # altrimenti input ha sempre lo stesso valore e non si raggiunge mai la condizione
    # per interrompere il ciclo, cioè un input vuoto che mette in azione il break
    if (parola):
        # perché con ifa parola io controllo che l'input sia pieno
        parole.append(parola.lower())
    else:
        break
    
for parola in parole:
    print(parola)