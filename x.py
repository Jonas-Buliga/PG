if __name__ == "__main__":

    def prumer():
        return sum(student["znamky"]) / len(student["znamky"])

    def naformatuj_text():
        return f"Student {student['jmeno']} {student['prijmeni']}, Vek {student['vek']}, Obor: {student['obor']}, Prumer: {prumer():.1f}"

    student = {
        "jmeno": "Jan",
        "prijmeni": "Novak",
        "vek": 22,
        "znamky": [1, 2, 3, 1, 2, 1]
    }

    student["vek"] += 1
    student["obor"] = "AEFP"

    print(student)
    print(naformatuj_text())
