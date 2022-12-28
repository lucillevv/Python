grootste = 0
kleinste = 0
deelbaar = 0

for x in range(1, 11):
    num = int(input("geef getal nummer {} in = ".format(x)))
    if num % 3 == 0:
        deelbaar += 1
    if x == 1:
        kleinste = num
        grootste = num
    elif num < kleinste:
        kleinste = num
    elif num > grootste:
        grootste = num

print("het grootste getal is = ", grootste)
print("het kleinste getal is = ", kleinste)
print("aantal getallen deelbaar door 3 zijn = ", deelbaar)
