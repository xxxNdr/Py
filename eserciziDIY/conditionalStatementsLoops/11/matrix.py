import numpy as np

row = int(input("inserisci un numero di righe"))
col = int(input("inserisci un numero di colonne"))

matrix = np.zeros((row, col), dtype=int)
# la funzione zeros di numpy serve a creare array o matrici
# prende come parametri la dimensione del vettore o della matrice
# restituisce un array numpy con i valori impostati a zero
# dtype=int fa sì che i valoria siano interi perché di default sono float


for x in range(col):
    for y in range(row):
        matrix[y,x] = x*y
        # bisogna usare questa sintassi se l'array è creato con numpy
        # numpy usa gli indici per accedere a elementi della matrice
        # numpy e python leggono gli indici nel formato [riga, colonna]
        # quindi devo scrivere matrix[y,x] e non l'opposto
        # matrix[y,x] = x*y significa: usare gli indici di righe e colonne per scrivere il prodotto tra gli indici
        # la dimensione della matrice e la posizione delle cifre viene data dalla dimensione dei range dei cili for

print(matrix)