# Opdracht 3 condities
# Naam student:
# Groep:

normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

leeftijd = int(input("Geef uw leeftijd in aantal jaar\n"))

if 0 <= leeftijd <= 2:
    groep = "baby"
    korting = 100
elif 3 <= leeftijd <= 18:
    groep = "kinderen"
    korting = 50
elif 19 <= leeftijd <= 64:
    groep = "volwassenen"
    korting = 0
elif 65 <= leeftijd <= 150:
    groep = "ouderen"
    korting = 30
else:
    groep = "onbekend"
    korting = 0

prijs = normale_toegangsprijs * (1 - korting / 100)

print(f"U behoort tot de groep {groep}")
print(f"U krijgt {korting}% korting")
print(f"U betaalt {prijs}")
