def stringati(n, base):
    string = "0123456789ABCDEF"
    if n < base:
        return string[n]
    else:
        return stringati(n // base, base) + string[n % base]


# Facendo la conversione passo passo di (2835, 16)

# 2835÷16=177
# 2835÷16=177 con resto 3
# 3 ← questa è la cifra meno significativa (l'ultimo carattere, cioè "3")

# 177÷16=11
# 177÷16=11 con resto 1
# 1 ← questa è la cifra successiva (il "1")

# 11÷16=0
# 11÷16=0 con resto 11
# 11 ← questa è la cifra più significativa, ma 11 in esadecimale si rappresenta con la lettera B


print(stringati(16, 2))

# 16 // 2=8 + 0
# 8 // 2=4 + 0
# 4 // 2=2 + 0
# 2 // 2=1 + 0
# 1 // 2=0 + 1
# res = 10000

# praticamente il resto della divisione viene usato come indice nella scala esadecimale
# per restituire un valore corrispondente
