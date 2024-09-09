"""FourDirections"""
def directions(tid):
    """FourDirections"""
    row_1 = ""
    row_2 = ""
    row_3 = ""
    row_4 = ""
    row_5 = ""
    center_row_rl = "*" * 5
    center_row_ud = "*" + " " + "*" + " " + "*"
    for i in tid:
        row_1 += f"{'*':^5}"
        row_5 += f"{'*':^5}"
        if i in ("U", "D"):
            row_3 += center_row_ud
            if i == "U":
                row_2 += f"{'***':^5}"
                row_4 += f"{'*':^5}"
            else:
                row_2 += f"{'*':^5}"
                row_4 += f"{'***':^5}"
        if i in ("L", "R"):
            row_3 += center_row_rl
            if i == "L":
                row_2 += f"{' *':<5}"
                row_4 += f"{' *':<5}"
            else:
                row_2 += f"{'* ':>5}"
                row_4 += f"{'* ':>5}"
        row_1 += " "
        row_2 += " "
        row_3 += " "
        row_4 += " "
        row_5 += " "
    print(row_1)
    print(row_2)
    print(row_3)
    print(row_4)
    print(row_5)
directions(input())
