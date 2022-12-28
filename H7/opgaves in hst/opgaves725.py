num = int(input("geef een getal"))
total = 0

for i in range(3):
    num = int(input("geef een getal"))
    total += num
print(total)

# deze lukt nooit????

for x in range(21, 0, -3):
    print(x)


num = int(input("geef een getal "))

for i in range(num, -1, -1):
    print(i)
    if i == 0:
        print("start")
