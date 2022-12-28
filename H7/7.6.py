woord1 = input("geef een eerste woord ")
woord2 = input("geef een tweede woord ")

common = ""

for letter in woord1:
    if (letter in woord2) and (letter not in common):
        common += letter
if common == 0:
    print("de woorden hebben geen tekens gemeen")
else:
    print("de woorden hebben de volgende letters gemeen:", common)
