from random import randint

tests = 500000
succes = 0

for x in range(tests):
    firstdice = 0
    for i in range(1, 6):
        throw = randint(1, 6)
        if throw < firstdice:
            break
        firstdice = throw
    else:
        succes += 1

print("de waarschijnlijkheid is", succes / tests)
