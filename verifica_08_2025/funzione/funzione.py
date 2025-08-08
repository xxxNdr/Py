

def t(testo : str):

    alnum = 0
    for x in testo:
        if x.isalnum():
            alnum += 1

    lunghezzaTotale = len(testo)

    parole = testo.split()
    paroleDiverse = set(parole)     # insieme non ordinato di elementi unici

    paroleMaiuscola = []

    for x in testo.split():
        if x[0].isupper():
            paroleMaiuscola.append(x)

    letterA = testo.count("a") + testo.count("A")
    bytes = len(testo.encode())

    print()
    print(repr(testo))
    print()
    print(f"Lunghezza totale: {lunghezzaTotale} caratteri")
    print(f"Caratteri alfanumerici: {alnum}")
    print(f"Parole distinte: {len(paroleDiverse)} parole")
    print(f"Parole con maiuscola: {len(paroleMaiuscola)} = {', ' .join(paroleMaiuscola)}")
    print(f"La lettera 'a' compare {letterA} volte")
    print(f"Il numero di byte per memorizzare questa stringa è di {bytes}")
    print()

t( """
    Nel mezzo del cammin di nostra vita
    mi ritrovai per una selva oscura, 
    chè la diritta via era smarrita.

    Ahi quanto a dir qual era è cosa dura
    esta selva selvaggia e aspra e forte
    che nel pensier rinova la paura!""" )