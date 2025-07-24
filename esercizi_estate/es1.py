lista = [[1,2,3],[4,5,6],[7,8,9]]

def p(lista):
    listaPiatta = []
    for x in lista:
        listaPiatta += x
    return listaPiatta

print(p(lista))