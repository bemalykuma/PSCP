"""PassWord"""
import math
def lower_(n):
    """lower"""
    ans = 0
    for i in n:
        if i.islower():
            ans = 26
    return ans

def upper_(n):
    """upper"""
    ans = 0
    for i in n:
        if i.isupper():
            ans = 26
    return ans

def number(n):
    """number"""
    ans = 0
    for i in n:
        if i.isnumeric():
            ans = 10
    return ans

def symbol(n):
    """key char"""
    ans = 0
    key = "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_","+","=","{","}","[","]"\
    ,"|", "/","\\",":",";","\"","\'","<",">",",",".","?","~"
    for i in n:
        if i in key:
            ans = 32
    return ans

def password(text):
    """Password"""
    length = len(text)
    r = lower_(text) + upper_(text) + number(text) + symbol(text)
    entropy = math.floor(math.log2(r**length))
    print(entropy)
    if entropy < 28:
        print("Very Weak")
    elif 28 <= entropy <= 35:
        print("Weak")
    elif 36 <= entropy <= 59:
        print("Reasonable")
    elif 60 <= entropy <= 127:
        print("Strong")
    elif entropy >= 128:
        print("Very Strong")
password(input())
