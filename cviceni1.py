def vysoky_nebo_nizky():
    vyska = int(input("Zadej výšku:"))
    if vyska > 180:
        print (f"Je vysoky.")
    elif vyska < 180:
        print (f"Neni vysoky.")
    else:
        print (f"Meri presne 180 cm.")

vysoky_nebo_nizky()