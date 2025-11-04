# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

# De rest moet jij doen.....
pogingen = 0
geraden = False

while not geraden:
    gok = int(input(prompt))
    pogingen += 1

    if gok < geheim_getal:
        print("hoger")
    elif gok > geheim_getal:
        print("lager")
    else:
        print(f"Je hebt het getal geraden! Het is {geheim_getal}!")
        print(f"Je hebt het in {pogingen} keer gedaan.")
        geraden = True

        # schrijf het resultaat naar een tekstbestand
        with open("raad_getal_resultaten.txt", "a") as bestand:
            bestand.write(f"Het getal was {geheim_getal}, geraden in {pogingen} pogingen.\n")

print("Resultaat is opgeslagen in raad_getal_resultaten.txt")


