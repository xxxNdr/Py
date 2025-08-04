testo = """Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura,
chè la diritta via era smarrita.
  
Ahi quanto a dir qual era è cosa dura
esta selva selvaggia e aspra e forte
che nel pensier rinova la paura!"""

print(len(testo))
print(repr(testo))
print(len(testo.encode()))  # Numero di byte in UTF-8
count_alfanumerici = sum(1 for c in testo if c.isalnum())
print(count_alfanumerici)
