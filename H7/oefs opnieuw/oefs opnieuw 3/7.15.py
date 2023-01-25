piraten = 5
kokos = 0

while True:
    kokos += 1
    stapel = kokos
    for x in range(5):
        if stapel % piraten != 1:
            break
        stapel = (piraten - 1) * int((stapel - 1) / piraten)
    if stapel % piraten == 1:
        break
print(kokos)
