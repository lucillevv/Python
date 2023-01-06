word = input("Input a word to reverse: ")

for x in range(len(word) - 1, -1, -1):
    print(word[x], end="")
print("\n")

# de -1 zijn de arguments van range
# len = loop gaat zolang door als de lengte van de string
# [] print enkel dat teken van de string
