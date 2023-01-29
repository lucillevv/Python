sum = 0

for x in range(2):
    num = int(input("geef een getal "))
    sum += num

if sum in range(15, 20):
    print("sum is 20")
else:
    print(sum)
