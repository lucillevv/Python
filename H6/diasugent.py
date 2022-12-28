woord = input("geef een woord")

if len(woord) <= 5:
    print("dit is een kort woord")
if len(woord) > 5:
    print("dit is een lang woord")

a = int(input("geef een getal in"))
b = int(input("geef een getal in"))

grootste = 0

if a > b:
    grootste = a
else:
    grootste = b
print(grootste)
