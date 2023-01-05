from random import randint

tests = 10000
succes = 0

for i in range(tests):
    lastdice = 0
    for j in range(5):
        roll = randint(1, 6)
        if roll < lastdice:
            break
        lastdice = roll
    else:
        succes += 1

print("de kans is", succes / tests)
