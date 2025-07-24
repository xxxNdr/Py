def data(giorni:int,mesi:int,anno:int):
    if giorni >= 1 and giorni <= 31:
        giorniS = str(giorni) + '/'
    else:
        raise ValueError("Devi inserire un numero compreso tra 1 e 31")
    if mesi >= 1 and mesi <= 12:
        mesiS = str(mesi) + '/'
    else:
        raise ValueError("Devi inserire un numero compreso tra 1 e 12")
    if anno >= 0:
        annoS = str(anno)
        data = giorniS + mesiS + annoS
        return data
            

print(data(1,12,2025))
print(data(35,2,2002))