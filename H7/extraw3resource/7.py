datalist = [
    1452,
    11.23,
    1 + 2j,
    True,
    "w3resource",
    (0, -1),
    [5, 12],
    {"class": "V", "section": "A"},
]

for x in datalist:
    print("{} = {}".format(x, type(x).__name__), sep="\n")

# .__name__ doet de <class> weg bij type, andere optie is str(type(x)) en dan
# specifieren met [] welke range specifieke karakters je wil afdrukken, denk [8:-2]
