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

# functie om de oppervlakte en inhoud van vierkant te bereken
def vierkant(oppervlakte,inhoud):
    zijde = int(input("Geef de zijde "))
    if oppervlakte == "OPP":
        opp = zijde**2
        return opp
    elif inhoud == "INHOUD":
        inh = zijde**3
        return inh



# functie die de prijs vna het materiaal bepaalt
def materiaalprijs(oppervlakte,materiaal,hoogte):
    if materiaal ==  "HOUT":
        prijs = (oppervlakte * 100) + (hoogte - 150)* 0.02
        return prijs
    elif materiaal == "STAAL":
        prijs = (oppervlakte * 115) + (hoogte - 150)* 0.02
        return prijs

# functie die de inhoud berekent


def graafwerken(inhoud):
    prijs = inhoud * 60
    return prijs

def plaatsingskost(inhoud):
    if inhoud > 100:
        prijs = inhoud * 15
        return prijs
    elif inhoud <= 100:
        prijs = inhoud * 18
        return prijs
    elif inhoud <= 50:
        prijs = inhoud * 20
        return prijs

print(vierkant("oppervlakte","inhoud"))




vorm = input("Welke vorm zwembad wens je? (V)ierkant, (R)echthoek, (C)ircel ")
mtrl = input("Welke materiaalsoort wens je? HOUT of STAAL ")
hgt = int(input("Hoe hoog wil je je zwembad? "))