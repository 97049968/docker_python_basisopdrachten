#!/usr/bin/env python3
# Dit is de module
# In dit bestand komen alle functies.
# Je kunt de functies in een ander .py bestand gebruiken door te starten  met:
# from my_modules import csv

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

def filter_persoon(lijst, filterveld, filtertekst):
    """
    Filtert de lijst van personen op basis van het filterveld en filtertekst.
    Geeft een lijst van volledige namen terug.
    """
    resultaat = []
    for persoon in lijst:
        if filtertekst.lower() in persoon.get(filterveld, "").lower():
            resultaat.append(volledige_naam(persoon))
    return resultaat
