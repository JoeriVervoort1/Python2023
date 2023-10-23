import random   # import random module

lst = []        # lege lijst

for getal in range(47):     # loop om 47 getallen in lijst toe te voegen
    x = random.randrange(20,200)    # random getallen tussen 20 en 200
    lst.append(x)       # toevoeging in de lege lijst

for i in range(3):      # 3 maal een getal laten ingeven
    y = int(input("Geef een getal in "))
    lst.append(y)       # getallen bij toevoegen aan de lijst

lst.sort(reverse=True)      # sorteren van de lijst in omgekeerde volgorde

print(lst[0:3])             # afdrukken van de drie grootste getallen
gemiddelde = sum(lst)/50    # berekenen van het gemiddelde van de lijst
print(gemiddelde)           # afdrukken van het gemiddelde van de lijst
print(lst)                  # afdrukken van de gesorteerde lijst
