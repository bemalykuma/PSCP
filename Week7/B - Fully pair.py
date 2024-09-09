'''B - Fully pair?'''
def pair(text):
    '''B - Fully pair?'''
    ans = ""
    while text:
        if text.count(text[0]) % 2:
            ans += text[0]
        else:
            ans += ""
        text = text.replace(text[0],"")
    if not ans:
        ans = "fully paired"
    print(ans)
pair(input())
