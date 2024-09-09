"""Bubble"""
def bubble(jump):
    """bubble"""
    count = 0
    left = 0 #เหลือ
    i = 0
    ans = ""
    while i < len(jump)-1:
        if jump[i] == "^":
            if jump[i+1] == "|":
                ans = "POSSIBLE"
                count += 1
            else:
                count += 1
                i += 1
        if jump[i] == "o":
            if jump[i+1] == "|":
                count += 1
                i += 1
                ans = "POSSIBLE"
            elif jump[i+1] == " ":
                left = len(jump[i+1:])
                ans = "IMPOSSIBLE"
            else:
                i += 1
                count += 1
        if jump[i] == "O":
            if i+3 <= len(jump):
                if jump[i+3] in ("o","O","|"):
                    count += 1
                    i += 3
            elif i+2 <= len(jump) and jump[i+2] in ("o", "O", "|"):
                count += 1
                i += 2
            elif jump[i+1] in ("o", "O", "|"):
                count += 1
                i += 1
            elif jump[i+1] == " " and jump[i+2] == " " and jump[i+3] == " ":
                left = len(jump[i+1:])
                ans = "IMPOSSIBLE"
        if ans in ("POSSIBLE", "IMPOSSIBLE"):
            break
    if jump[i] == "|":
        ans = "POSSIBLE"
        left = count
    print(ans)
    print(left)
bubble(input())
