# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

tekst = input("Geef de tekst die je wilt encrypten\n")
versleuteld = ""

for letter in tekst:
    if letter.islower():  # kleine letters
        nieuwe_letter = chr((ord(letter) - ord('a') + 5) % 26 + ord('a'))
        versleuteld += nieuwe_letter
    elif letter.isupper():  # hoofdletters
        nieuwe_letter = chr((ord(letter) - ord('A') + 5) % 26 + ord('A'))
        versleuteld += nieuwe_letter
    else:  # spaties of leestekens blijven hetzelfde
        versleuteld += letter

print("Versleutelde tekst:", versleuteld)
