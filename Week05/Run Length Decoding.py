"""Run Length Decoding"""
def decoding(code):
    """Run Length Decoding"""
    result = ""
    num = ""
    for i in code:
        if i.isnumeric():
            num += i
            amount = int(num)
        else:
            result += i * amount
            num = ""
    print(result)
decoding(str(input()))
