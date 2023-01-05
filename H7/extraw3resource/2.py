maat = input("welke temp wilt u omzetten? (F of C): ")
temp = int(input("hoeveel graden?: "))

C = 0
F = 0

if maat == "F":
    C = (5 / 9) * (temp - 32)
    print(C)
elif maat == "C":
    F = (9 * temp) / 5 + 32
    print(F)
