totaal = 0
gem = 0
n = 0
num = int(input("geef een getal "))

while num != 0:
    totaal += num
    n += 1
    gem = totaal / n
    num = int(input("geef een getal "))

print(gem, totaal)
