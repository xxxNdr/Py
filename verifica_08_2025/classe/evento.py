class Evento:
    def __init__(s, nome:str, data:str, luogo:str, posti_totali:int, prezzo:float) -> None:
        s.nome = nome
        s.data = data
        s.luogo = luogo
        s.posti_totali = posti_totali
        s.posti_prenotati = 0
        s.prezzo = prezzo

    def posti_disponibili(s):
        return s.posti_totali - s.posti_prenotati
        
    
    def prenota(s, numero_posti):
        if numero_posti <= 0:
             print("Richiesta impossibile\n")
             return False
        
        disponibili = s.posti_disponibili()
        if numero_posti <= disponibili:
                s.posti_prenotati += numero_posti
                print(f"Hai correttamente prenotato {numero_posti} posti\n")
                return True
        else:
            print(f"Non ci sono abbastanza posti diponibili: {disponibili} / richiesti: {numero_posti}\n")
            return False
        
    def annulla_prenotazione(s, numero_posti):
         if numero_posti <= s.posti_prenotati:
              s.posti_prenotati -= numero_posti
              print(f"Hai correttamente annullato {numero_posti} prenotazioni\n")
              return True
         else:
              print("Non puoi annullare più posti di quanti ne hai prenotati\n")
              return False
    
    def calcola_incasso(s):
        tot = s.posti_prenotati * s.prezzo
        print(f"L'incasso totale per l'evento di {s.nome} è di {tot} €\n")

    def ottieni_info_evento(s):
        tot = s.posti_prenotati * s.prezzo
        potenziale = s.posti_disponibili() * s.prezzo
        print(f"Evento: {s.nome}\nData: {s.data}\nLuogo: {s.luogo}\nPosti totali: {s.posti_totali}\nPosti prenotati: {s.posti_prenotati}\nIncasso attuale: {tot} €\nIncasso stimato: > {potenziale} €\n")







e1 = Evento("Kate Perry", "2/11/2025","Unipol Arena", 18000, 74.75)

print(e1.posti_disponibili())
e1.prenota(10)
print(e1.posti_disponibili())
e1.annulla_prenotazione(5)
print(e1.posti_disponibili())
(e1.calcola_incasso())
e1.ottieni_info_evento()
