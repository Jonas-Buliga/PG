

if __name__ == "__main__":

    def prumer(znamky):
        return sum(znamky) / len(znamky)

    def naformatuj_text(student):
        jmeno = student["jmeno"]
        prijmeni = student["prijmeni"]
        vek = student["vek"]
        obor = student["obor"]
        znamky = student["znamky"] 
        prumer_znamky = round(prumer(znamky), 2)
        text = f"Student: {jmeno} {prijmeni}, Vek: {vek}, Obor: {obor}, Prumer: {prumer_znamky}"
        return text
    
    student = {
        "jmeno": "Jan",
        "prijmeni": "Novak",
        "vek": 22,
        "znamky": [1, 2, 3, 1, 2, 1]
    }

    student["vek"] += 1
    student["obor"] = "AEFP"


    print(naformatuj_text(student))























    
    #seznam = [100, 5, 3, 21]

    #seznam[2] *= 2

    #seznam.append(55)

    #seznam.sort()
    #seznam.reverse()

    #print(seznam)