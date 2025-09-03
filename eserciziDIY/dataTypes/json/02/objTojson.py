import json

andrea = {
    "nome" : "andrea",
    "classe" : "fsd",
    "eta" : "38"
}

print(type(andrea))

andre = json.dumps(andrea)

print(andre)

# dumps prende l'oggetto e lo trasforma in stringa json
# se volessi scrivere direttamente su un file json invece dovrei usare dump

with open("andrea.json", "w") as file:
    json.dump(andrea, file)