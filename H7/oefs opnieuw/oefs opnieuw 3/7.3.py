grootste = 0
kleinse = 0
deler = 0

for x in range(1, 11):
    num = int(input("geef getal nummer {}: ".format(x)))
    if num % 3 == 0:
        deler += 1
    if x == 1:
        kleinste = num
        grootste = num
    elif kleinste > num:
        kleinste = num
    elif grootste < num:
        grootste = num
print(
    "de grootste is {}, kleinste {} en aantal deelbaar door 3 is {}".format(
        grootste, kleinste, deler
    )
)
