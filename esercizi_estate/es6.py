def mediaPond(peso_valore: dict):
    prodotti = []
    for peso, valore in peso_valore.items():
        if not (isinstance(peso, int) and isinstance(valore, int)):
            raise ValueError("Chiave e valore devono essere entrambi interi")
        prodotti.append(peso * valore)
    sommaProdotti = sum(prodotti)
    sommaPesi = sum(peso_valore.keys())
    return sommaProdotti / sommaPesi


# Esempio di dati
dati = {1:30, 2:36, 3:31, 4:38}

print(mediaPond(dati))