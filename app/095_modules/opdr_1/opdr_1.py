# Opdracht 1 functies
# Naam student:
# Groep:

# importeer de module csv...
# opdr_1.py

# importeer onze module
from my_modules import csv

# lijst van personen
namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

# print alle volledige namen
for persoon in namen:
    print(csv.volledige_naam(persoon))
