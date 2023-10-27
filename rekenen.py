import random

def optellen1(optellen):
    while optellen != "stop":
        x = random.randint(0,10)
        y = random.randint(0,10)
        if x > 5 and y > 5:
            y = random.randint(0,5)
        print(x ,"+", y)
        z = (input(""))
        if z == "stop":
            break
        else:
            z = int(z)
        if z == (x+y):
            print("Goed zo Laura <3")
        else:
            print("probeer opnieuw")
def aftrekken(aftrekken):
    while aftrekken != "stop":
        x = random.randint(0,10)
        y = random.randint(0,10)
        while x < y:
            y = random.randint(0,10)
        print(x ,"-", y)
        z = (input(""))
        if z == "stop":
            break
        else:
            z = int(z)
        if z == (x - y):
            print("Goed zo Laura <3")
        else:
            print("probeer opnieuw")

rekenen = input("Wil je optellen of aftrekken of stoppen? ")
if rekenen == "optellen":
    optellen1("optellen")
elif rekenen == "aftrekken":
    aftrekken("aftrekken")



