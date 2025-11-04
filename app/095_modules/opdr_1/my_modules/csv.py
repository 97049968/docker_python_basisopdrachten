# my_modules/csv.py

def volledige_naam(persoon):
    """
    Geeft de volledige naam van een persoon (dictionary) terug als string.
    Verwijdert dubbele spaties als tussenvoegsel leeg is.
    """
    voornaam = persoon["voornaam"]
    tussenvoegsel = persoon["tussenvoegsel"]
    achternaam = persoon["achternaam"]
    
    if tussenvoegsel:
        return f"{voornaam} {tussenvoegsel} {achternaam}"
    else:
        return f"{voornaam} {achternaam}"
