w1 = input("geef het eerste woord")
w2 = input("geef het tweede woord")

beide = ""

for letter in w1:
    if (letter in w2) and (letter not in beide):
        beide += letter
if beide == 0:
    print("de woorden hebben niks gemeen")
else:
    print("de woorden hebben de volgende tekens gemeen:", beide)
