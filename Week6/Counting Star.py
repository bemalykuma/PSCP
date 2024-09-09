"""counting star"""
def star(code):
    """counting star"""
    cons = 0
    comet = 0
    shoot = 0
    collect = ""
    for i in code:
        collect += i
        if " " in collect:
            collect = ""
        if "*~" in collect or "~*" in collect:
            comet += 1
            collect = ""
        elif "*/" in collect:
            shoot += 1
            collect = ""
        elif "**" in collect:
            cons += 1
            collect = ""
    if not comet and not shoot and not cons:
        print("Tonight is a quiet night.")
    else:
        print(f"constellation: {cons}")
        print(f"comet: {comet}")
        print(f"shooting star: {shoot}")
star(input())
