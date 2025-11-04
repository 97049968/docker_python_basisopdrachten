# Opdracht 4 condities
# Naam student:
# Groep:

toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = []
for t in toppings:
    beschikbare_toppings.append(t[0])

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings}\n")

# Hier de rest van jouw code...
gevonden = False

for t in toppings:
    if keuze == t[0]:
        print(f"U heeft {t[0]} besteld. Dat kost {t[1]}")
        gevonden = True

if not gevonden:
    print("Uw keuze zit niet in ons assortiment")
