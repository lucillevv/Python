s = "s"

for i in range(10, 0, -1):
    print("{0} flesje{1} met bier op de muur, {0} flesje{1} met bier.".format(i, s))
    if i == 1:
        s = ""
    elif i == 0:
        s = "s"
        i = "geen"
    print(
        "Open er een, drink hem meteen, {} flesje{} met bier op de muur.".format(
            i - 1, s
        )
    )
# niet juist
