# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

gasten = ["Jij", "Paul", "Kees", "Marie", "Hilda"]
print(gasten)

#Marie gaat niet meer mee:
gasten.remove("Marie")
print(gasten)

#George wil mee, en wil naast Kees zitten
gasten.insert(gasten.index("Kees") + 1, "George")
print(gasten)