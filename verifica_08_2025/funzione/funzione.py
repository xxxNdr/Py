def t(testo : str):
    lunghezzaTotale = len(testo)
    parole = testo.split()
    paroleDiverse = set(parole)
    paroleMaiuscola = []
    for parola in testo.split():
        if parola[0].isupper():
            paroleMaiuscola.append(parola)
    letterA = testo.count("a") + testo.count("A")
    bytes = len(testo.encode()) 
    print()
    print(repr(testo))
    print()
    print(f"Lunghezza Totale: {lunghezzaTotale} caratteri")
    print(f"Parole distinte: {len(paroleDiverse)} parole")
    print(f"Parole con maiuscola: {len(paroleMaiuscola)} = {', ' .join(paroleMaiuscola)}")
    print(f"La lettera 'a' compare {letterA} volte")
    print(f"Il numero di bytes per memorizzare questa stringa è di {bytes}")
    print()

t('''Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura,
chè la diritta via era smarrita.
  
Ahi quanto a dir qual era è cosa dura
esta selva selvaggia e aspra e forte
che nel pensier rinova la paura!''')