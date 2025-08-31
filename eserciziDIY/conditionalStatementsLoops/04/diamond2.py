for x in range(1,6):
    for y in range(x):
        print('*', end=' ')
    print()
for x in range(4,0,-1):
    for y in range(x):
        print('*', end=' ')
    print()

# il ciclo si muove da 1 a 5
# per ogni valore che ha assunto x dal ciclo esterno vengono stampati tot asterischi (y)
# al primo giro x sarà range 1 e quindi ci saranno 1 y nel range x da stampare
# stampa l'asterisco e termina con uno spazio perché invece print di default aggiunge alla fine \n
# questo print fuori dal ciclo interno ma dentro il ciclo esterno serve per andare a capo
# dopo ogni iterazione di y nel range di x
# infine il movimento speculare contrario del codice scritto sopra
