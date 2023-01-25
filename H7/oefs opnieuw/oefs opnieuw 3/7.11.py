num = int(input("geef een getal in voor een matrix "))

print(".", "|", end="")
for x in range(1, num + 1):
    print("{:2}".format(x), end=" ")
print()
for i in range(4 * x):
    print("-", end="")
print()
for j in range(1, num + 1):
    print(j, "|", end=" ")
    for y in range(1, num + 1):
        print("{:^2}".format(j * y), end=" ", sep="\n")
    print()
