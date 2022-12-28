flesjes = 99
s = "s"

while flesjes != 0:
    if flesjes == 1:
        s = ""
        print(
            "{0} flesje{1} met bier op de muur, {0} flesje{1} met bier.".format(
                flesjes, s
            )
        )
    else:
        print(
            "{0} flesje{1} met bier op de muur, {0} flesje{1} met bier.".format(
                flesjes, s
            )
        )
    flesjes -= 1
    if flesjes == 1:
        s = ""
        print(
            "Open er een, drink hem meteen, {0} flesje{1} met bier op de muur.".format(
                flesjes, s
            )
        )
    else:
        s = "s"
        print(
            "Open er een, drink hem meteen, {0} flesje{1} met bier op de muur.".format(
                flesjes, s
            )
        )
