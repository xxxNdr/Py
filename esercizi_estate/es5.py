def ep(evento:str, *partecipanti:str):
    ris = f"Evento: {evento}\n"
    for p in partecipanti:
        ris += f" - {p}\n"
    ereturn ris



print(ep('Pizza di classe', 'marco', 'giannino', 'stefano', 'stega', 'andrea'))