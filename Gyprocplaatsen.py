import math

# functie om de plaatsingskost te berekenen
def plaatsingskost(opp,dikte):
    platen = math.ceil(opp / 1.44)      # berekenen van het aantal platen naar boven afgerond
    if dikte == 6:                      # berekening van de prijs van de platen en plaatsing voor 6mm
        prijsplt = platen * 5.8
        prijsplts = opp * 6.2
        return prijsplt + prijsplts
    elif dikte == 9:                    # berekening van de prijs van de platen en plaatsing voor 9mm
        prijsplt = platen * 7.4
        prijsplts = opp * 7.3
        return prijsplt + prijsplts
    elif dikte == 12:                   # berekening van de prijs van de platen en plaatsing voor 12mm
        prijsplt = platen * 8.3
        prijsplts = opp * 7.8
        return prijsplt + prijsplts

# functie om de vervoerskost te bereken
def vervoersprijs(afstand):     # berekening voor van de prijs tot 10 km
    if afstand <= 10:
        prijs = 5
        return prijs
    elif afstand > 10:          # berekening van de prijs boven 10 km
        prijs1 = (afstand - 10) * 0.3
        prijs = prijs1 + 5
        return prijs

# main programma
opp = int(input("Hoeveel vierkante meter? "))
keuze = int(input("Welke platen? 6 of 9 of 12 "))
afstd = int(input("Hoever is het in km? "))

prijstotaal = plaatsingskost(opp,keuze) + vervoersprijs(afstd)
print("De totaalprijs bedraagt ",prijstotaal,"€")