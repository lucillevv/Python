woord = input("geef een woord ")


for x in range(len(woord) - 1, -1, -1):
    print(woord[x], end="")
print("\n")
