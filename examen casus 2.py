
# functie om de aanspreking te bepalen
def aanspreking(geslacht,Familie_naam,beroep):
    lst = []
    if geslacht == "MAN":
        lst.append("Heer")      # toevoeging van Heer in lijst
    else:
        lst.append("Mevrouw")   # toevoeging van Mevrouw in lijst
    if beroep == "DOKTER":
        lst.append("Dr.")       # toevoeging van Dr. in de lijst
    elif beroep == "PROFESSOR":
        lst.append("Prof.")     # toevoeging van Prof. in lijst
    elif beroep == "INGENIEUR":
        lst.append("Ir")        # toevoeging van Ir. in lijst
    else:
        lst.append("")          # toevoeging zonder aanspreking
    lst.append(Familie_naam)

    print("Geachte",lst[0],lst[1],lst[2])       # Afdrukken van de lijst met Aanspreking

for i in range(3):              # for loop om 3 x de gegevens te vragen
    geslacht = input("Wat is je geslacht? ")
    Familie_naam = input("Wat is je familienaam? ")
    beroep = input("Wat is je beroep? ")
    aanspreking(geslacht.upper(),Familie_naam.capitalize(),beroep.upper())   # Uitvoeren van de functie in hoofdletters en capitalized