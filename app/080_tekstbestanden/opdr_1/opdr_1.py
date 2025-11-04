# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

vraag1 = input("Wat vind je van de huidige regering?\n")
vraag2 = input("Wat vind je van de Python-lessen tot nu toe?\n")
vraag3 = input("Wat vind jij de mooiste stad van Nederland?\n")

bestand = open("enquete_resultaten.txt", "w")
bestand.write("Resultaten van de enquete:\n")
bestand.write(f"1. Wat vind je van de huidige regering? {vraag1}\n")
bestand.write(f"2. Wat vind je van de Python-lessen tot nu toe? {vraag2}\n")
bestand.write(f"3. Wat vind jij de mooiste stad van Nederland? {vraag3}\n")
bestand.close()

print("Bedankt voor het invullen! De resultaten zijn opgeslagen in enquete_resultaten.txt")

