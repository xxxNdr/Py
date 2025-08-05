class Libro:
    def __init__(s, titolo, autore, annoPubblicazione : int, isbn : int, disponibilita : bool):
        s.titolo = titolo
        s.autore = autore
        s.annoPubblicazione = annoPubblicazione
        s.isbn = isbn
        s.disponibilita = disponibilita
        
    def info(s) -> str:
        stato = "Disponibile" if s.disponibilita else "Non disponibile"
        return f"\ntitolo: {s.titolo}\nautore: {s.autore}\nanno di pubblicazione: {s.annoPubblicazione}\nisbn: {s.isbn}\nstato: {stato}\n"
    
    def presta(s) -> bool:
        if s.disponibilita:
            s.disponibilita = False
            print(f"Hai preso in prestito:\n{s.titolo}\ndi {s.autore}\n")
            return True
        else:
            print(f"\nNon puoi prendere in prestito:\n{s.titolo}\ndi {s.autore}\n")
            return False



libro1 = Libro("Il nome della rosa", "Umberto Eco", 1980, 8831459759, True)
print(libro1.info())
libro1.presta()
print(libro1.disponibilita)
libro1.presta()

libro2 = Libro("La fattoria degli animali", "George Orwell", 1945,  9788804796664, False)


class Biblioteca:
    pass