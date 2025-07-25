from typing import Any

# modulo typing solo per annotare i paramettri della funzione
# Any: accetto qualsiasi tipo di dato

def prodotto(nome:str, **dettagli:Any):
    
    righe = [f"Prodotto: {nome}"]
    for k, v in dettagli.items():
        if k.lower() == 'stato':
            friendly = 'Disponibile' if v else 'Non disponibile'
            # Solo se la chiave è 'stato',
            # Rinomino v in friendly
            # e stampo Disponibile se è True, altrimenti Non disponibile,
        else:
            friendly = v
            # Se la chiave non è 'stato' allora friendly è uguale a v
        leggibile = k.replace('_', ' ').capitalize()
        # sostituisci ogni underscore in k con uno spazio e aggiungi prima lettera maiuscola a k
        righe.append(f"{leggibile}: {friendly}")
    print('\n' + '\n'.join(righe) + '\n')


# argomenti passati come keywords nel dizionario detagli
prodotto("Samsung", modello="A55", memoria="500GB", costo="499€", stato=False, quantità_in_negozio=5)
