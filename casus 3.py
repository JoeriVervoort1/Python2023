import math
"""Kies de vorm van het zwembad: vierkant (V), rechthoekig (R), circel (C).
Kies het Materiaal: Staal of Hout.
	Prijs per m²: hout €100, staal €115.
	Hoogste standaard: 150 cm, elke centimeter erboven + 2 procent.
Graafwerken € 60 per m³ 10*10*1,6= 160*60 = € 9600
	Plaatsingskost:  <= 50 m³= €20 per m³
		  <=100m³ = €18 per m³
		>100m³ = € 15 per m³
Druk de kostprijs van het zwembad, de graafkosten en plaatsingskosten en
de totaalprijs van het project af. """

def vierkant(hgt):      # functie om de oppervlakte en inhoud van vierkant te bereken
    lst = []
    zijde = float(input("Geef de zijde "))
    opp = zijde**2
    lst.append(opp)
    inh = zijde**2 * (hgt/100)                      # hoogte is in cm dus delen door 100 voor m
    lst.append(inh)
    return lst                                      # teruggave van de lijst met oppervlakte en inhoud

def rechthoek(hgt):     # functie om de oppervlakte en inhoud van rechthoek te berekenen
    lst = []
    breedte = float(input("Geef de breedte "))
    lengte = float(input("Geef de lengte "))
    opp = breedte * lengte
    lst.append(opp)
    inh = breedte * lengte * (hgt/100)               # hoogte is in cm dus delen door 100 voor m
    lst.append(inh)
    return lst                                      # teruggave van de lijst met oppervlakte en inhoud

def circel(hgt):        # functie om de oppervlakte en inhoud van een circel te berekenen
    lst = []
    diameter = float(input("Geef de diameter "))
    opp = (diameter/2)**2 * math.pi                 # diamter delen door 2 om straal te berekenen
    lst.append(opp)
    inh = (diameter/2)**2 * math.pi * (hgt/100)     # hoogte is in cm dus delen door 100 voor m
    lst.append(inh)
    return lst

def materiaalprijs(oppervlakte,materiaal,hoogte):   # functie die de prijs van het materiaal bepaalt
    hgtprct = (hoogte - 150) * 2                    # berekening van het extra percentage boven 150cm
    if materiaal ==  "HOUT":
        prijsopp = (oppervlakte * 100)              # berekening van de prijs ver vkm
        prijstotaal = prijsopp * hgtprct / 100 + prijsopp   # berekening van de totaal prijs incl hoogte prct
        return prijstotaal
    elif materiaal == "STAAL":
        prijsopp = (oppervlakte * 115)              # berekening van de prijs ver vkm
        prijstotaal = prijsopp * hgtprct / 100 + prijsopp   # berekening van de totaal prijs incl hoogte prct
        return prijstotaal

def graafwerken(inhoud):                            # functie om de graafwerken te bereken
    prijs = inhoud * 60
    return prijs

def plaatsingskost(inhoud):                         # functie op de plaatsingskost te berekenen
    if inhoud <= 50:
        prijs = inhoud * 20
        return prijs
    elif inhoud <= 100:
        prijs = inhoud * 18
        return prijs
    elif inhoud > 100:
        prijs = inhoud * 15
        return prijs

vorm = input("Welke vorm zwembad wens je? (V)ierkant, (R)echthoek, (C)ircel ")
mtrl = input("Welke materiaalsoort wens je? HOUT of STAAL ")
hgt = float(input("Hoe hoog wil je je zwembad in cm? "))
lst = []                # lege lijst om opp en inhoud op te slaan
lst1 = []
lstprijs = []           # lege lijst om de prijzen in op te slaan

# prijsberekening adh van vorm, inhoud toegevoegd aan lstprijs met graafwerken en plaatsingskost
if vorm.upper() == "V" and mtrl.upper() == "HOUT":
    lst = vierkant(hgt)
    prijs_per_vkm = materiaalprijs(lst[0],"HOUT",hgt)
    lstprijs.append(prijs_per_vkm)
    lstprijs.append(graafwerken(lst[1]))
    lstprijs.append(plaatsingskost(lst[1]))
elif vorm.upper() == "V" and mtrl.upper() == "STAAL":
    lst = vierkant(hgt)
    prijs_per_vkm = materiaalprijs(lst[0],"STAAL",hgt)
    lstprijs.append(prijs_per_vkm)
    lstprijs.append(graafwerken(lst[1]))
    lstprijs.append(plaatsingskost(lst[1]))
elif vorm.upper() == "R" and mtrl.upper() == "HOUT":
    lst = rechthoek(hgt)
    prijs_per_vkm = materiaalprijs(lst[0], "HOUT", hgt)
    lstprijs.append(prijs_per_vkm)
    lstprijs.append(graafwerken(lst[1]))
    lstprijs.append(plaatsingskost(lst[1]))
elif vorm.upper() == "R" and mtrl.upper() == "STAAL":
    lst = rechthoek(hgt)
    prijs_per_vkm = materiaalprijs(lst[0], "STAAL", hgt)
    lstprijs.append(prijs_per_vkm)
    lstprijs.append(graafwerken(lst[1]))
    lstprijs.append(plaatsingskost(lst[1]))
elif vorm.upper() == "C" and mtrl.upper() == "HOUT":
    lst = circel(hgt)
    prijs_per_vkm = materiaalprijs(lst[0], "HOUT", hgt)
    lstprijs.append(prijs_per_vkm)
    lstprijs.append(graafwerken(lst[1]))
    lstprijs.append(plaatsingskost(lst[1]))
elif vorm.upper() == "C" and mtrl.upper() == "STAAL":
    lst = circel(hgt)
    prijs_per_vkm = materiaalprijs(lst[0], "STAAL", hgt)
    lstprijs.append(prijs_per_vkm)
    lstprijs.append(graafwerken(lst[1]))
    lstprijs.append(plaatsingskost(lst[1]))

print("de materiaalkost bedraagt ",round(lstprijs[0],2),"€")
print("de graafwerken kosten ",round(lstprijs[1],2),"€")
print("de plaatsingskost bedraagt ",round(lstprijs[2],2),"€")
print("de totaalprijs bedraagt ",round(sum(lstprijs),2),"€")