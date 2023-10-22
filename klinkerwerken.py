"""Een klinkerwerker legt op 1 uur, 12 m², zijn uurtarief bedraag 40 euro per uur btw in.
Er zijn 3 maten in klinker
10x10 cm: 14euro per m²
12x12 cm: 16euro per m²
14x14 cm 16,5euro per m²
Indien er oude klinker of kiezels verwijdert moeten worden telt hij het uur prijs, hij verwijderd 15m² per uur.
Voor het vervoer vraag hij 5 euro + 0,30 cent per km boven de 10 km.
De werkuren worden samengeteld indien hij legt en verwijderd. Werkuren worden altijd naar boven afgerond"""
import math

# functie die het uurtarief berekent
def werkuren(opp,afbraak):
    prijs1 = math.ceil(opp / 12) * 40  # uurprijs inclusief btw
    if afbraak == "NEE":    # zonder verwijderen van oude kiezel/klinkers
        return prijs1
    elif afbraak == "JA":   # met verwijderen oude kiezel/klinkers
        prijs2 = math.ceil(opp / 15) * 40
        return prijs1 + prijs2

# functie die de klinkerprijs berekent ahv oppervlakte
def klinkerprijs(keuze,opp):
    if keuze == "A":       # prijsberekening voor klinker 10 x 10
        prijs = opp * 14
        return prijs
    elif keuze == "B":      # prijsberekening voor klinker 12x12
        prijs = opp * 16
        return prijs
    else:                   # prijsberekening voor klinker 14 x 14
        prijs = opp * 16.5
        return prijs

# functie die de vervoersprijs berekent
def vervoersprijs(afstand):     # berekening voor van de prijs tot 10 km
    if afstand <= 10:
        prijs = 5
        return prijs
    elif afstand > 10:          # berekening van de prijs boven 10 km
        prijs1 = (afstand - 10) * 0.3
        prijs = prijs1 + 5
        return prijs

# main programma

opp = float(input("Hoeveel vierkante meter? "))
keuze = input("Welke klinker? 10x10(A), 12x12(B), 14x14(C) ")
afbraak = input("moet er oude kiezel/klinkers verwijderd worden? JA of NEE ")
afstd = float(input("Hoever is het in km? "))

prijs_totaal = werkuren(opp,afbraak.upper()) + klinkerprijs(keuze.upper(),opp) + vervoersprijs(afstd)
print("De totaalprijs is ",round(prijs_totaal,2),"€")