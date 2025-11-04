# Opdracht 1 modules
# Naam student:
# Groep:

# import .....
# for line in open("test.csv", 'rt'):
#   jouw code komt hier!

# opdr_1.py

from my_modules import csv

namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk", "plaats": "Amsterdam"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra", "plaats": "Den Haag"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas", "plaats": "Delft"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet", "plaats": "Rotterdam"},
    {"voornaam": "Jan", "tussenvoegsel": "Van Der", "achternaam": "Vliet", "plaats": "Dordrecht"},
]

# Filter voorbeelden
resultaat1 = csv.filter_persoon(namen, "voornaam", "ja")
resultaat2 = csv.filter_persoon(namen, "voornaam", "Pie")  # voorbeeld, kan leeg zijn
resultaat3 = csv.filter_persoon(namen, "plaats", "d")

print("Filter voornaam 'ja':")
for r in resultaat1:
    print(r)

print("\nFilter voornaam 'Pie':")
for r in resultaat2:
    print(r)

print("\nFilter plaats 'd':")
for r in resultaat3:
    print(r)
