cijfer = float(input("geef een getal in "))

if cijfer < 0 or cijfer > 10:
    print("cijfer moet binnen 0 en 1O liggen")
elif cijfer % 0.5 != 0:
    print("cijfers moeten afgrond zijn naar dichtste 0.5")
elif cijfer <= 5:
    print("je hebt een F")
elif cijfer <= 6:
    print("cijfer is een D")
elif cijfer <= 7:
    print("cijfer is een C")
elif cijfer <= 8:
    print("cijfer is een B")
else:
    print("cijfer is een A")
