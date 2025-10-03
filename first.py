def sudy_nebo_lichy(cislo):
    if cislo % 2 == 0:
        return f"Číslo {cislo} je sudé."
    else:
        return f"Číslo {cislo} je liché."

# Volání funkce
print(sudy_nebo_lichy(5))
print(sudy_nebo_lichy(1000000))
