num = int(input("geef een getal voor een matrix: "))

print(".", "|", end=" ")
for x in range(1, num + 1):
    print("{:^2}".format(x), end=" ")
print()
print(4 * num * "-")
for i in range(1, num + 1):
    print(i, "|", end=" ")
    for j in range(1, num + 1):
        print("{:^2}".format(i * j), end=" ")
    print()
