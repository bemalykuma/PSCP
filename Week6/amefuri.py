"""Amefuri ตากผ้าดีมั้ย"""
def morning(h):
    """in the morning"""
    wet = 0
    if h.lower() == "c":
        wet -= 0.50
    elif h.lower() == "n":
        wet -= 1.00
    elif h.lower() == "w":
        wet -= 1.50
    return wet

def night(h):
    """in the night"""
    wet = 0
    if h.lower() == "c":
        wet -= 0.25
    elif h.lower() == "n":
        wet -= 0.50
    elif h.lower() == "w":
        wet -= 0.75
    return wet

def rainy(h):
    """if raining"""
    wet = 0
    if h.lower() == "r":
        wet += 2.00
    if h.lower() == "s":
        wet += 3.00
    return wet

def takpa(start, log):
    """Dry clothes"""
    wet = 8
    for i in log:
        if start > 24:
            start -= 24
        if 6 <= start < 18:
            wet += morning(i)
        if 0 <= start < 6 or 18 <= start <= 24:
            wet += night(i)
        if i.lower() in ("r","s"):
            wet += rainy(i)
        if i.lower() == "h":
            ans = "Lost"
            break
        if wet <= 0:
            ans = "Dry"
            break
        if wet > 0:
            ans = f"Still Wet (Wet Level: {wet:.02f})"
        if wet > 16:
            wet = 16
        start += 1
    print(ans)
takpa(int(input()), input())
