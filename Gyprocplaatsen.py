import math

# functie om de plaatsingskost te berekenen
def plaatsingskost(opp,dikte):
    if dikte == 6:
        platen = float(opp / 1,44)
        prijs = math.ceil(platen) * 6.2
        return prijs

print(plaatsingskost(20,6))