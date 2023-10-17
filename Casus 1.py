"""Looptijden:
Geef het aantal deelnemers in.
Geef de looptijd in minuten in.
Sla alle tijden op in een lijst
Geef de 3 snelste tijden.
Geef de gemiddelde tijd"""

deelnemers = int(input("Geef het aantal deelnmers ")) # Vraagt het aantal deelnemers

lst1 = [] # Lijst van tijden per deelnemer

# Vraag per loper de gelopen tijd en zet in lst1
for loper in range(deelnemers):
    x = int(input("Geef de tijd "))
    lst1.append(x)

# Sorteer lst1 in oplopende volgorde
lst1.sort()

# Print de 3 snelste tijden
for tijd in lst1[0:3]:
    print("De snelste tijden zijn : ",tijd)

# Print de gemiddelde tijd van alle deelners
gemiddelde = sum(lst1)/deelnemers
print("De gemiddelde tijd bedraagt : ",round(gemiddelde))