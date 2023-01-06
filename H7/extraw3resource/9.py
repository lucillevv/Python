# Fibonacci

num1 = 0
num2 = 1

print(num1, num2, end=" ")

while True:
    num3 = num1 + num2
    if num3 > 50:
        break
    print(num3, end=" ")
    num1 = num2
    num2 = num3
