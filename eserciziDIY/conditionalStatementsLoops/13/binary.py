divisibili = []

num = input("inserisci diversi numeri binari separati da virgola").split(",")
# input ha una duplice funzione: presenta un messaggio, prompt, all'utente
# e raccoglie i dati dall'utente sottoforma di stringa

for x in num:
    x = int(x, 2)
    # converti in intero decimale un numero a base binaria. Importante!
    if not x % 5:
        # equivale a scrivere if num % 5 == 0
        # (perché not 0 è sinonimo di not false quindi true)
        x = bin(x)[2:]
        divisibili.append(x)
print(divisibili)
