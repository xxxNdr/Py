temp = (
    input("inserisci la temperatura che vuoi convertire")
    .strip()
    .lower()
    .replace(" ", "")
)
gradi = int(temp[:-1])
convenzione = temp[-1]

if convenzione == "c":
    fahre = (gradi * 9 / 5) + 32
    print(f"{round(fahre, 2)}F")
elif convenzione == "f":
    cel = (gradi - 32) * 5 / 9
    print(f"{round(cel, 2)}C°")
else:
    print("unità di misira non riconosciuta")
