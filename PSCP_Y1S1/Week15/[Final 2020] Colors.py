'''[Final 2020] Colors'''
def color(cl_1, cl_2):
    '''Mix Colors'''
    list_color = ["Yellow", "Blue", "Red"]
    if cl_1 in list_color and cl_2 in list_color and cl_1 == cl_2:
        print(cl_1)
    elif cl_1 in ("Yellow", "Blue") and cl_2 in ("Yellow", "Blue"):
        print("Green")
    elif cl_1 in ("Yellow", "Red") and cl_2 in ("Yellow", "Red"):
        print("Orange")
    elif cl_1 in ("Blue", "Red") and cl_2 in ("Blue", "Red"):
        print("Violet")
    else:
        print("Error")
color(input(), input())
