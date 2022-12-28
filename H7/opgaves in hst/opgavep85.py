from pcinput import getInteger
from sys import exit

while True:
    x = getInteger("geef een getal: ")
    if x < 0:
        print("mag niet")
        continue
    else:
        break
print(x)
