import random

def optellen1(optellen):
    while optellen != "stop":
        x = random.randint(0,10)
        y = random.randint(0,10)
        if x > 5 and y > 5:
            y = random.randint(0,5)
        return x,y

lst = (optellen1(1))
print(lst,0,"+",lst,1)
z = int(input(""))
if z == sum(lst):
    print("Goed zo Laura <3")


