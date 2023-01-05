groot = 0
klein = 0
deler = 0

for i in range(1, 11):
    num = int(input("geef een getal"))
    if num % 3 == 0:
        deler += 1
    if i == 1:
        klein = num
        groot = num
    elif num < klein:
        klein = num
    elif num > groot:
        groot = num

print("de grootste is {}, kleinste is {} en delers zijn {}".format(groot, klein, deler))
