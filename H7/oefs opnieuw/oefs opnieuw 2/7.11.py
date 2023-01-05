num = int(input("geef een getal "))

print("•", "|", end="")

for i in range(1, num + 1):
    print("{:^2}".format(i), end=" ")
print()
for i in range(3 * (num + 1)):
    print("-", end="")
print()
for i in range(1, num + 1):
    print(i, "|", end="")
    for j in range(1, num + 1):
        print("{:<2}".format(i * j), end=" ")
    print()
