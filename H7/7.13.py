from random import randint

tests = 1000
kans = 0

for i in range(tests):
    lastdice = 0
    for x in range(5):
        roll = randint(1, 6)
        if roll < lastdice:
            break
        lastdice = roll
    else:
        kans += 1
print("het aantal kansen dat dit gebeurt is ", kans / tests)
