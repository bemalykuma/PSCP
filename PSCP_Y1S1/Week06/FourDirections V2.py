"""FourDirections"""
def directions(tid):
    """FourDirections"""
    up = ["  *  "," *** ","* * *","  *  ","  *  "]
    down = ["  *  ","  *  ","* * *"," *** ","  *  "]
    left = ["  *  ", " *   ", "*****", " *   ","  *  "]
    right = ["  *  ", "   * ", "*****", "   * ","  *  "]
    for i in range(5):
        for j in tid:
            if j == "U":
                print(up[i], end = " ")
            elif j == "D":
                print(down[i], end = " ")
            elif j == "L":
                print(left[i], end = " ")
            else:
                print(right[i], end = " ")
        print()
directions(input())
