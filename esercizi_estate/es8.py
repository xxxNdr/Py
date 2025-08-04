def aggiornaImpostazioni(impostazioniAttuali:dict, **nuoveImpostazioni):
    impostazioniAttuali.update(nuoveImpostazioni)
    output = ""
    for k, v in impostazioniAttuali.items():
        output += f"{k}: {v}\n" 
    return output


rubrica = {'nome': 'Alice',
           'eta': 30}

risultato = aggiornaImpostazioni(rubrica, citta='Bologna', eta=38, gruppo_sanguineo='AB+')

print(risultato)