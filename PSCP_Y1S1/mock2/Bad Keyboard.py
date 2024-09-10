"""Bad Keyboard"""
def keyboard(text):
    """Bad Keyboard"""
    ans = ""
    for i in text:
        if i == "o":
            i = i.replace("o", "i")
        elif i == "O":
            i = i.replace("O", "I")
        elif i == "i":
            i = i.replace("i", "o")
        elif i == "I":
            i = i.replace("I", "O")
        ans += i
    print(ans)
keyboard(input())
