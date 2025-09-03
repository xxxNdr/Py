import json

andrea = '{"nome": "andrea", "età": "38", "città": "bologna"}'
andre = json.loads(andrea)

print(type(andre))
print(andre["nome"])

# in questo modo la stringa json diventa un dizionario al quale posso accedere
# inserendo una chiave
# la differenza tra load e loads è che il primo deserializza un json in oggetto partendo da un file
# metre il secondo converte una stringa json in oggetto