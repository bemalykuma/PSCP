'''CaesarV1'''
def upper_(n, shift):
    '''Alpha_Upper'''
    tmp = ord(n) + shift
    while tmp > 90:
        tmp -= 26
    while tmp < 65:
        tmp += 26
    ans = chr(tmp)
    return ans

def lower_(n, shift):
    '''Alpha_Lower'''
    tmp = ord(n) + shift
    while tmp > 122:
        tmp -= 26
    while tmp < 97:
        tmp += 26
    ans = chr(tmp)
    return ans

def ceasar(shift, text):
    '''CaesarV1'''
    ans = ""
    for i in text:
        if i.isalpha() and i.isupper():
            ans += upper_(i, shift)
        elif i.isalpha() and i.islower():
            ans += lower_(i, shift)
        else:
            ans += i
    print(ans)
ceasar(int(input()), input())
