human = int(input("how many years is your dog "))

dog = 0

for years in range(human):
    if years < 2:
        dog += 10.5
    else:
        dog += 4
print("The dog's age in dog's years is", round(dog))
