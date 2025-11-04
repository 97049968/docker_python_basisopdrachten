# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

antwoorden = {}

for i, vraag in enumerate(vragen, start=1):
    antwoord = input(f"{i}. {vraag}\n")
    if "voornaam" in vraag.lower():
        antwoorden["voornaam"] = antwoord
    elif "achternaam" in vraag.lower():
        antwoorden["achternaam"] = antwoord
    elif "drank" in vraag.lower():
        antwoorden["drank"] = antwoord
    elif "eten" in vraag.lower():
        antwoorden["eten"] = antwoord

with open("party.txt", "a") as bestand:
    bestand.write("----\n")
    bestand.write(f"voornaam: {antwoorden['voornaam']}\n")
    bestand.write(f"achternaam: {antwoorden['achternaam']}\n")
    bestand.write(f"drank: {antwoorden['drank']}\n")
    bestand.write(f"eten: {antwoorden['eten']}\n\n")

print("\nBedankt voor het invullen!\nSee you at the party.")
