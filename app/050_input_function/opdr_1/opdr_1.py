# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.
import math

a = float(input("Geef de lengte van de eerste zijde\n"))
b = float(input("Geef de lengte van de tweede zijde\n"))

berekening = math.sqrt(a**2 + b**2)

if berekening.is_integer():
    print(f"De lengte van de schuine zijde is: {round(berekening)}")
else:
    print(f"De lengte van de schuine zijde is: {berekening}")
