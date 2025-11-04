# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

input = input("Geef minimaal 5 objecten, gescheiden door een komma:\n")

lijst = [item.strip() for item in input.split(",")]

lijst_sorted = sorted(lijst, reverse=True)

print(lijst_sorted)
