def cislo_text(cislo):
    jednotky = {
        0: 'nula', 1: 'jedna', 2: 'dva', 3: 'tři', 4: 'čtyři',
        5: 'pět', 6: 'šest', 7: 'sedm', 8: 'osm', 9: 'devět', 10: 'deset', 11: 'jedenáct',
        12: 'dvanáct', 13: 'třináct', 14: 'čtrnáct', 15: 'patnáct', 16: 'šestnáct',
        17: 'sedmnáct', 18: 'osmnáct', 19: 'devatenáct'
    }
    desitky = {
        2: 'dvacet', 3: 'třicet', 4: 'čtyřicet', 5: 'padesát',
        6: 'šedesát', 7: 'sedmdesát', 8: 'osmdesát', 9: 'devadesát'
    }

    if cislo < 20:
        return jednotky[cislo]
    elif cislo < 100:
        desitky_c = cislo // 10
        jednotka_c = cislo % 10
        if jednotka_c == 0:
            return desitky[desitky_c]
        else:
            return f"{desitky[desitky_c]} {jednotky[jednotka_c]}"
    elif cislo == 100:
        return "sto"
    else:
        return "neznámé číslo"


if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))  
    text = cislo_text(cislo)
    print(text)