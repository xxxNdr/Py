class Evento:
    def __init__(s, nome:str, data:str, posti_totali:int, prezzo:float) -> None:
        s.nome = nome
        s.data = data
        s.posti_totali = posti_totali
        s.posti_prenotati = 0
        s.prezzo = prezzo

    def posti_disponibili(s):
        return s.posti_totali - s.posti_prenotati
        
    
    def prenota(s, numero_posti):
        if numero_posti <= 0:
             print("Richiesta impossibile")
             return False
        
        disponibili = s.posti_disponibili()
        if numero_posti <= disponibili:
                s.posti_prenotati += numero_posti
                print(f"Hai correttamente prenotato {numero_posti} posti")
                return True
        else:
            print(f"Non ci sono abbastanza posti diponibili: {disponibili} / richiesti: {numero_posti}")
            return False
        
    def annulla_prenotazione(s, numero_posti):
         if numero_posti <= s.posti_prenotati:
              s.posti_prenotati -= numero_posti
              print(f"Hai correttamente annullato {numero_posti} prenotazioni")
              return True
         else:
              print("Non puoi annullare più posti di quanti ne hai prenotati")
              return False
    
    def calcola_incasso(s):
         







e1 = Evento("Kate Perry", "2/11/2025", 18000, 74.75)

print(e1.posti_disponibili())
e1.prenota(10)
print(e1.posti_disponibili())
e1.annulla_prenotazione(5)
print(e1.posti_disponibili())

