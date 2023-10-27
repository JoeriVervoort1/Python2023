# functie om de waarde van de waarborg terug te geven aan het hoofdprogramme
def waarborg(type):
    if type == "KINDERFIETS":
        prijs = 100
        return prijs
    elif type == "VOLWASSENFIETS" or type == "TANDEM":
        prijs =  150
        return prijs
    elif type == "ELECTRISCHE":
        prijs = 200
        return prijs
    elif type == "PEDELEC":
        prijs = 350
        return prijs

# functie die de prijs van het verhuur per type berekent
def verhuurfiets(type,dagen,verzekering):
    if type == "KINDERFIETS" and verzekering == "JA":       # prijsberekening kinderfiets met verzekering
        prijs = (dagen * 30) + (dagen * 8)
        return prijs
    elif type == "KINDERFIETS":                             # prijsberekening kinderfiets zonder verzekering
        prijs = dagen * 30
        return prijs
    elif type == "VOLWASSENFIETS" and verzekering == "JA":  # prijsberekening volwassenfiets met verzekering
        prijs = (dagen * 40) + (dagen * 10)
        return prijs
    elif type == "VOLWASSENFIETS":                          # prijsberekening volwassenfiets zonder verzekering
        prijs = dagen * 40
        return prijs
    elif type == "TANDEM" and verzekering == "JA":          # prijsberekening tandem met verzekering
        prijs = (dagen * 50) + (dagen * 10)
        return prijs
    elif type == "ELECTRISCHE" and verzekering == "JA":     # prijsberekening electrische fiets met verzekering
        prijs = (dagen * 50) + (dagen * 15)
        return prijs
    elif type == "TANDEM" or type == "ELECTRISCHE":         # prijsberekening tandem en electrische fiets zonder verzekering
        prijs = dagen * 50
        return prijs
    elif type == "PEDELEC" and verzekering == "JA":         # prijsberekening pedelec met verzekering indien rijbewijs ok is
        rbws = input("Heb je een rijbewijs? ")
        if rbws == "JA":
            prijs = (dagen * 70) + (dagen * 25)
            return prijs
        else:
            print("Pedelec is niet toegestaan, electrische fiets in de plaats")   # vervanging pedelec naar electrische fiets met vrzkg
            prijs = (dagen * 50) + (dagen * 15)
            return prijs
    elif type == "PEDELEC":                                 # prijsberekening pedelec zonder verzekering indien rijbewijs ok
        rbws = input("Heb je een rijbewijs? ")
        if rbws == "JA":
            prijs = (dagen * 70)
            return prijs
        else:
            print("Pedelec is niet toegestaan, electrische fiets in de plaats")     # vervanging pedelec naar electrische fiets zonder vrzkg
            prijs = (dagen * 50)
            return prijs

# Hoofdprogramma
aantal = int(input("Hoeveel fietsen wens je te huren? "))
lst = []                                                        # lege lijst om de prijzen in op te slaan
x = 0
for x in range(aantal):                                         # for loop om door het ingegeven aantal fietsen te gaan
    type = input("Welke fiets wens je? ")
    dagen = int(input("Hoeveel dagen wens je de fiets? "))
    vrzkg = input("Wens je een verzekering? ")
    totaalprijs = verhuurfiets(type.upper(),dagen,vrzkg.upper()) + waarborg(type.upper())   # oproepen van de functies om de prijs te berekenen
    x = x + 1
    lst.append(totaalprijs)                                     # toevoegen van de prijs per fiets in de lege lijst
y = 0
for i in lst:                                                   # for loop om door de lijst te gaan
    y += 1
    print("fiets",y,i,"€")                                      # printen van de prijs per fiets
print("De totaal prijs bedraagt",sum(lst),"€")               # printen van de totaalprijs