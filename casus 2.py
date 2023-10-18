"""Gebruiker kiest een categorie: A: Ford Fiesta, B: Ford Focus, C: Ford Puma, D: Ford Kuga
Prijs per dag A: 55 euro, B: 70 euro, C: 80 euro, D: 90 euro.
Prijs per KM gereden: 0,18 euro 20 km gratis. C en D  hebben 50 km gratis.
All-in pakket met verzekering: A en B + 25 euro per dag, C en D + 40 euro per dag.
	+ 100 km gratis(Voor alle categorieën) in totaal(dus niet per dag)
De gebruiker simuleert 3 autos: Zet de totaalprijzen in een lijst.
Druk ze vervolgens regel per regel af met optie 1,2,3"""

# functie om de prijs per dag te bepalen per categorie
def prijs_per_dagen_per_km(categorie,aantal_dagen,aantal_kilometer):
    if categorie == "A":
        prijs = (55 * aantal_dagen) + ((aantal_kilometer - 20)* 0.18)
        return prijs
    elif categorie == "B":
        prijs = (70 * aantal_dagen) + ((aantal_kilometer - 20)* 0.18)
        return prijs
    elif categorie == "C":
        prijs = (80 * aantal_dagen) + ((aantal_kilometer - 50)* 0.18)
        return prijs
    elif categorie == "D":
        prijs = (90 * aantal_dagen) + ((aantal_kilometer - 50)* 0.18)
        return prijs
    else:
        print("Verkeerde categorie")

# functie die de indien gewenste verzekering de prijs bepaalt
def all_in_pakket(verzekering,categorie,aantal_dagen):
        if verzekering == "NEE":
            prijs = 0
            return prijs
        elif verzekering == "JA" and categorie == "A" or categorie == "B":
            prijs = 25 * aantal_dagen - 80 * 0.18
            return prijs
        elif verzekering == "JA" and categorie == "B" or categorie == "C":
            prijs = 40 * aantal_dagen - 80 * 0.18
            return prijs

# main pgrm
lst = [] # lijst waar de prijzen in worden opgeslagen

for x in range(0,1):
    ctgr = input("Welke categorie kies je? A, of B, of C, of D ")  # vraag de categorie
    dgn = int(input("Hoeveel dagen wens je de auto ")) # vraag het aantal dagen
    km = int(input("Hoeveel kilometers wil je rijden? "))  # vraag het aantal kilometers
    vzk = input("Wens je een all in pakket? JA of NEE ")
    ctgr = ctgr.upper()
    vzk = vzk.upper()
    prs1 = lst.append((prijs_per_dagen_per_km(ctgr,dgn,km)) + (all_in_pakket(vzk,ctgr,dgn)))


for i in lst:
    print(i)