"""US Interstate Number System"""
def major(w):
    """Major Interstates"""
    if w[-1] == "0" and w != "00" and w != "0" :
        ans = "Horizontal Major Interstate"
    elif w[-1] == "5":
        ans = "Vertical Major Interstate"
    else:
        ans = "Others"
    return ans

def minor(w):
    """Minor Interstates"""
    if w[-1] == "0" and w[1:] != "00" or w[-1] == "5":
        if int(w[:1]) % 2:
            ans = "Odd Minor Interstate"
        else:
            ans = "Even Minor Interstate"
    else:
        ans = "Others"
    return ans

def highway(way):
    """high way"""
    parent = ""
    way_digits = len(way)
    if way_digits <= 2:
        ans = major(way)
        parent = f"I-{int(way)}"
    elif way_digits == 3:
        ans = minor(way)
        parent = f"I-{int(way[1:])}"
    else:
        ans = "Others"
    print(ans)
    if ans != "Others":
        print(parent)
highway(input())
