"""Frame"""
def main(text):
    """Frame"""
    text_l = len(text)
    print("*" * (text_l+2))
    print(f"*{text}*")
    print("*" * (text_l+2))
main(str(input()))
