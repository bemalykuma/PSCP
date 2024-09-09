"""Future Message"""
def main(text):
    """Future Message"""
    if text.isnumeric():
        print("Number")
    elif text.isupper():
        print("Uppercase")
    elif text.islower():
        print("Lowercase")
    elif text.istitle():
        print("Title")
    elif " " in text:
        print("Space")
    else:
        print("Other")
main(input())
