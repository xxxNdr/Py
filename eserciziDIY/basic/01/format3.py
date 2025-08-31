def format(testo, parole_formattare):
    for x in parole_formattare:
        testo = testo.replace(x, x + "\n\t")
    return testo + '\n\t'


testo = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are!"
parole = ["star,"]
parole2 = ["high,"]
parole3 = ["sky."]

parti = testo.split("are!", 1)
parte1 = parti[0] + "are!"

forma1 = format(parte1, parole)

parti2 = parti[1].split("high,", 1)
parte2 = parti2[0] + "high,"

forma2 = format(parte2, parole2).rstrip()

parti3 = parti2[1].split("sky", 1)
parte3 = parti3[0] + "sky."

forma3 = format(parte3, parole3).rstrip()

print(forma1 + '\t' + forma2 + '\n\t\t' + forma3 + '\n' + forma1 )
