totaal = 0
for i in (12, 4, 3, 33, -2, -5, 7, 22, 4):
    if i == 0:
        print("klaar")
        break
    if i < 0:
        continue
    totaal += i
else:
    print(totaal)
