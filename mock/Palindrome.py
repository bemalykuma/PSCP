"""Palindrome"""
def palindrome(num,text):
    """Palindrome"""
    text = text.replace(":","")
    length_text = len(text)
    ans = ""
    i = 0
    while i < num:
        text = int(text)
        text += 1
        if length_text == 3:
            text = f"{text:>03}"
        natee =  int(str(text)[-2:])
        if natee >= 60:
            hour = int(str(text)[:-2])
            text = int(str(hour+1) + f"{str(natee - 60):>02}")
            if text >= 2400:
                text -= 2400
                length_text = len(f"{text:>03}")
        if length_text == 3:
            text = f"{text:>03}"
        elif length_text == 4:
            text = f"{text:>04}"
        if text == text[::-1]: #Check Palindrome
            length = len(text)
            for j in range(length):
                if j == length//2:
                    ans += ":" + text[j]
                else:
                    ans += text[j]
            print(ans)
            i += 1
            ans = ""
palindrome(int(input()), input())
