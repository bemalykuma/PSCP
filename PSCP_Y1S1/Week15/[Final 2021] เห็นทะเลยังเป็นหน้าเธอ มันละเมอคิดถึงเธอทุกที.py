'''[Final 2021] เห็นทะเลยังเป็นหน้าเธอ มันละเมอคิดถึงเธอทุกที'''
def shark(fishing):
    '''[Final 2021] เห็นทะเลยังเป็นหน้าเธอ มันละเมอคิดถึงเธอทุกที'''
    shallow = "BULL SHARK"
    twilight = "CHAIN CATSHARK", "GREAT WHITE SHARK", "GUMMY SHARK", "BLUE SHARK", "MAKO SHARK"
    midnight = "FRILLED SHARK", "GOBLIN SHARK", "SIXGILL SHARK", "GREENLAND SHARK", \
        "COOKIECUTTER SHARK"
    abyssal = "MEGAMOUTH SHARK"
    if fishing == shallow:
        print("THE SHALLOW ZONE")
    elif fishing == abyssal:
        print("THE ABYSSAL ZONE")
    elif fishing in twilight:
        print("THE TWILIGHT ZONE")
    elif fishing in midnight:
        print("THE MIDNIGHT ZONE")
    else:
        print("ZONE JAI MA KLUNG RAK DUAY KAN MAI.")
shark(input())
