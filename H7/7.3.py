min = 0
max = 0
deler = 0

for j in range(5):
    num = int(input("geef getal nummer {} in: ".format(j + 1)))
    if j == 0:
        min = num
        max = num
        continue
    if num % 3 == 0:
        deler += 1
    j += 1
    if num < min:
        min = num
    if num > max:
        max = num

print(min, max, deler)
