x,y = 0,1


for _ in range(0,10,1):
    print(x)
    x, y = y, x + y
# geniale, stampo subito x che alla prima iterazione è 0
# dopodiché x si aggiorna al valore di y che inizialmente è 1
# e y assume il nuovo valore (x+y) cioè 2
# nel prossimo ciclo stampo il nuovo valore di x che sarà 1
# e nel ciclo dopo sarà 1+2 e così via  