def sconto(prezzoStr:str, sconto:int):
    if sconto < 1 and sconto > 99:
        raise ValueError("Lo sconto deve essere un numero compreso tra 1 e 99")
    if prezzoStr.endswith('€'):
        prezzo = float(prezzoStr[:-1])
        valuta = '€'
    elif prezzoStr.endswith('$'):
        prezzo = float(prezzoStr[:-1])
        valuta = '$'
    else:
        raise ValueError("Il prezzo deve terminare con un $ o €")
    
    prezzo_scontato = prezzo * sconto / 100

    return f"{prezzo_scontato}{valuta}"

print(sconto('80 €', 40))