import random

# I, identifichiamo l'oggetto che dobbiamo gestire ---> devo aggiungere titolo e autore in ingresso all'init della classe libro
# Stiamo realizzando un software per una libreria, dobbiamo quindi gestire libri.


# II, implementiamo compra_da_fornitori.
# III, dove mi salvo i libri? Devo capire quale struttura dati devo utilizzare per
# ricordarmi ciò che ho acquistato.
# IV, implementiamo vendi_libri_nuovi

PREZZO_UNITARIO_LIBRO = 10                                      #costante
PREZZO_DI_VENDITA_UNITARIO = 20                                 #costante
PREZZO_DI_VENDITA_LIBRO_USATO = 12                              #costante # in buono stato


class Libro:
    def __init__(self, titolo, autore, prezzo, pagine, pagine_lette) -> None:
        self.titolo                                             = titolo
        self.autore                                             = autore
        self.prezzo                                             = prezzo
        self.pagine                                             = pagine
        self.pagine_lette                                       = pagine_lette                     

class Libreria:

  
    def __init__(self, investimento_iniziale) -> None:
        self.cassa                                              = investimento_iniziale
        self.libri_nuovi_da_vendere                             : list[Libro] = [ ]
        self.libri_usati_in_vendita                             : list[Libro] = [ ]


    def compra_da_fornitori(self, quantità, numero_copie):
        # devo comprare dal fornitore più copie di libri
        spesa_totale = quantità * numero_copie * PREZZO_UNITARIO_LIBRO

        if spesa_totale <= self.cassa:
        # posso comprare i libri
            for idx in range(quantità):
                for i in range(numero_copie):
                    self.libri_nuovi_da_vendere.append(Libro(f"Titolo-{idx}", f"Autore-{idx}" , f"Prezzo-{idx}"))
            # decremento i soldi in cassa
            self.cassa = self.cassa - spesa_totale

        else:
            print(f"Non è possibile comprare {quantità * numero_copie} libri")      # fast string

    def vendi_libro_nuovo(self, titolo_libro: str, autore_libro: str) -> Libro:
        # ricerca libri per titolo e autore, se ne trovo uno lo devo restituire in uscita

        indice_libro_trovato = -1                                                   #se rimane uguale a -1 il libro non è stato trovato

        for idx, libro_scelto in enumerate(self.libri_nuovi_da_vendere):
            
            # il libro cercato esiste tra quelli in vendita?
            if (libro_scelto.titolo == titolo_libro) and (libro_scelto.autore == autore_libro):
                # ho trovato il libro!
                indice_libro_trovato = idx
                # NON MODIFICATE MAI LA STESSA LISTA IN CUI STATE CERCANDO IL LIBRO!
                # PRIMA SALVARE L'INDICE E POI ACCEDERE ALLA LISTA
                break

        if indice_libro_trovato != -1:
            libro_da_vendere = self.libri_nuovi_da_vendere.pop(indice_libro_trovato)
            self.cassa = self.cassa + PREZZO_DI_VENDITA_UNITARIO
            return libro_da_vendere

        else:
            print(f"Libro dal titolo: {titolo_libro} e autore: {autore_libro} non trovato!")
            return Libro('','','')
        
        # Aggiornare cassa      /       # fatto, vedi sopra

    def vendi_libro_usato(self, titolo_libro, autore_libro):

        indice_libro_trovato = -1

        for idx, libro in enumerate(self.libri_usati_in_vendita):   
            if (libro.titolo == titolo_libro) and (libro.autore == autore_libro)
            indice_libro_trovato = idx
            break

        if indice_libro_trovato != -1:
            libro_usato_trovato = self.libri_usati_in_vendita.pop(indice_libro_trovato)
            self.cassa = self.cassa + PREZZO_DI_VENDITA_LIBRO_USATO
            return libro_usato_trovato
    
        else:
            print(f"Libro dal titolo: {titolo_libro} e autore: {autore_libro} non trovato!")
            return Libro('','','')

    def e_in_buono_stato(self, pagine, pagine_lette):
        if pagine_lette > pagine / 10:
            return 9
        else:
            return random.choice([0,1,2,3,4,5,6,7,8])
        
    def stima_prezzo_libro(self, _pagine, _pagine_lette):
        stato = e_in_buono_stato(self, _pagine, _pagine_lette)
        if stato == 0:
            print("Il libro è in condizioni pietose")
            return 0
        else:
            prezzo = stato * 1.5
            print(f"Il libro costa: {prezzo}")
            return prezzo


            
        
# libreria = Libreria(100)
# print("compro dai fornitori 2 libri di 2 copie ciascuno")
# libreria.compra_da_fornitori(2,2)

# print(20*"-")
# print(f"Cassa attuale: {libreria.cassa}")
# for libro in libreria.libri_nuovi_da_vendere:
#     print(libro.titolo)
#     print(libro.autore)

# print(20*"-")
# print("Vendiamo un libro")
# libro_acquistato = libreria.vendi_libro_nuovo('Titolo-0', 'Autore-0')
# print(libro_acquistato.titolo)
# print(libro_acquistato.autore)
# print(f"Cassa attuale: {libreria.cassa}")

# print(20*"-")
# print("Vendiamo un libro")
# libro_acquistato = libreria.vendi_libro_nuovo('HP', 'HP')
# print(libro_acquistato.titolo)
# print(libro_acquistato.autore)
# print(f"Cassa attuale: {libreria.cassa}")











    # 1, cerchiamo il libro corrispondente a autore_libro e titolo_libro
    # 2, se è in vendita, lo togliamo dalla merce nuova disponibile
    # 3, se non è in vendita lo comunichiamo al cliente
    # 4, restituiamo un libro al cliente se l'abbiamo trovato.
    # 5, aggiorniamo la cassa.





