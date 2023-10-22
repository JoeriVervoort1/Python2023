import random

def optellen1(optellen):
    while optellen != "stop":
        if optellen == "stop":
            break
        x = random.randint(0,10)
        y = random.randint(0,10)
        print(x ,"+", y)
        z = int(input(""))
        if z == (x+y):
            print("Goed zo Laura <3")
        else:
            print("probeer opnieuw")

def aftrekken(aftrekken):
    while aftrekken != "stop":
        if aftrekken == "stop":
            break
        x = random.randint(0,10)
        y = random.randint(0,10)
        print(x ,"-", y)
        z = int(input(""))
        if z == (x-y):
            print("Goed zo Laura <3")
        else:
            print("probeer opnieuw")

rekenen = input("Wil je optellen of aftrekken of stoppen? ")
if rekenen == "optellen":
    optellen1("optellen")
elif rekenen == "aftrekken":
    aftrekken("aftrekken")



