"""ValidVar"""
def validvar(num):
    """ValidVar"""
    w = "if", "else", "elif", "while", "for","continue", "break", "return", "is", "in", "and",\
        "or", "from","as", "pass", "not", "def","True", "False", "None"
    for _ in range(num):
        word = input()
        if word.isidentifier() is False or word in w :
            print("Invalid")
        else:
            print("Valid")
validvar(int(input()))
