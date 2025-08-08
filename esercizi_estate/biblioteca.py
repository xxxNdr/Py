class Libro:
    def __init__(
        s, titolo, autore, annoPubblicazione: int, isbn: int, disponibilita: bool
    ):
        s.titolo = titolo
        s.autore = autore
        s.annoPubblicazione = annoPubblicazione
        s.isbn = isbn
        s.disponibilita = disponibilita

    def __str__(s) -> str:
        return f"'{s.titolo}' di {s.autore} è in catalogo\n"

    def info(s) -> str:
        stato = "Disponibile" if s.disponibilita else "Non disponibile"
        return f"\ntitolo: '{s.titolo}'\nautore: {s.autore}\nanno di pubblicazione: {s.annoPubblicazione}\nisbn: {s.isbn}\nstato: {stato}\n"

    def presta(s) -> bool:
        if s.disponibilita:
            s.disponibilita = False
            print(f"Hai preso in prestito:\n'{s.titolo}'\ndi {s.autore}\n")
            return True
        else:
            print(f"\nNon puoi prendere in prestito:\n'{s.titolo}'\ndi {s.autore}\n")
            return False

    def restituisci(s) -> bool:

        if s.disponibilita == False:
            s.disponibilita = True
            print(f"Hai restituito:\n'{s.titolo}'\ndi {s.autore}\n")
            return True
        else:
            print("Non puoi restituire un libro che non è stato prestato\n")
            return False


libro1 = Libro("Il nome della rosa", "Umberto Eco", 1980, 8831459759, True)
print(libro1.info())
libro1.presta()
print(libro1.disponibilita)
libro1.presta()
libro1.restituisci()
print(libro1.disponibilita)
libro1.restituisci()

libro2 = Libro("La fattoria degli animali", "George Orwell", 1945, 9788804796664, False)
print(libro2.info())


class Biblioteca:
    def __init__(s, nome, catalogo=None):
        # MAI USARE OGGETTI MUTABILI COME VALORE DI DEFAULT
        # TRA I PARAMETRI DI FUNZIONI E METODI
        s.nome = nome
        if catalogo is not None:
            s.catalogo = catalogo
        else:
            s.catalogo = []

    def aggiungi(s, libro: Libro) -> bool:
        for x in s.catalogo:
            if x.titolo == libro.titolo and x.autore == libro.autore:
                print(f"'{libro.titolo}' è già presente in {s.nome}")
                return False
            continue

        s.catalogo.append(libro)
        print(f"Hai aggiunto '{libro.titolo}' al catalogo della {s.nome}\n")
        return True

    def rimuovi(s, libro):
        for x in s.catalogo:
            if x.isbn == libro.isbn:
                s.catalogo.remove(x)
                print(f"È stato rimosso '{libro.titolo}' dal catalogo\n")
                return True
            continue

        print(f"Non è possibile rimuovere un libro non presente in catalogo\n")
        return False

    def cerca(s, query, tipo):
        #
        # hasattr() serve a verificare se un oggetto possiede un attributo
        # la sintassi è: hasattr(oggetto, "nome_attributo")
        # oggetto è l'istanza o la classe da controllare
        # "nome_attributo" è una stringa che indica il nome dell'attributo da verificare
        # Es:
        # Class Persona:
        # nome = "Mario"
        # Mario = Persona()
        # print(hasattr(Mario, "cognome"))  -> False, perchè cognome non esiste
        #
        # getattr serve a leggere il valore di un attributo di un oggetto
        # modo dinamico di accedere a un attributo
        # la sintassi è: getattr(oggetto, nome_attributo, valore_default_opzionale)
        # valore_default è un valore che viene restituito se l'attributo non esiste
        # se l'attributo esiste, restituisce il suo valore equivalente a oggetto.nome_attributo
        # se non esiste usa il valore di default impostato, altrimenti genera errore AttributeError
        # Es:
        # Class Libro:
        # def __init__(self, titolo):
        # libro = Libro("1984")
        # print(getattr(libro, "titolo")) -> stampa "1984"
        # print(getattr(libro, "autore", "sconosciuto")) -> stampa sconosciuto perché autore non esiste
        # getattr può chiamare anche un metodo di una classe
        #
        ris = []
        for x in s.catalogo:
            if hasattr(x, tipo):
                valore = getattr(x, tipo, "Sconosciuto")
                if str(query).lower() in str(valore).lower():
                    # in è più utile di == perché trova corrispondenze pariali
                    # per una biblioteca è scomodo cercare una corrispondenza esatta
                    ris.append(x)
                    for x in ris:
                        print(x.info())
        else:
            # else si attiverebbe per ogni libro che non ha l'attributo che cerco
            # 
            print(f"Nessun {tipo} trovato in {s.nome} dalla tua ricerca\n")
        return ris


b1 = Biblioteca("Biblioteca Salaborsa", catalogo=None)
b1.aggiungi(libro1)

b1.aggiungi(libro2)

for libro in b1.catalogo:
    print(libro)

b1.rimuovi(libro2)
b1.cerca("il nome della rosa", "titolo")
