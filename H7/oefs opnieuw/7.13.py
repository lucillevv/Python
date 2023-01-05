from random import randint

tests = 10000
succes = 0

for x in range(tests):
    laatste = 0
    for y in range(5):
        throw = randint(1, 6)
        if throw < laatste:
            break
        laatste = throw
    else:
        succes += 1

print("de waarschijnlijkheid is", succes / tests)
