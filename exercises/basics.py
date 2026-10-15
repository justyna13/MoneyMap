# Ćwiczenia z podstaw Pythona.
# Uruchamiaj plik z terminala: python3 exercises/basics.py

# Zadanie: napisz pętlę for, która iteruje po liście ponizej
# i dla kazdego elementu wypisuje go razem z jego indeksem,
# np. w formacie "0: a", "1: b", "2: c"

litery = ["a", "b", "c"]

# Twoj kod ponizej:
for index, item in enumerate(litery):
    print(f"{index}: {item}")

def hello(imie: str) -> str:
    return f"Cześć, {imie}!"

print(hello("Anna"))

class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstaw_sie(self):
        return f"Cześć, jestem {self.imie} i mam {self.wiek} lat"

osoba = Osoba("Justyna", 28)


print(osoba.przedstaw_sie())

dane = {"imie": "Justyna", "wiek": 28}

try:
    print(dane["nazwisko"])
except KeyError as e:
    print(f"Brak klucza {e} w słowniku")
