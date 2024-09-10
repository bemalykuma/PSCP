"""Run Length Encoding"""
def encoding(code):
    """Run Length Encoding"""
    result = ""
    count = 0
    temp = code[0]
    for i in code:
        if i == temp:
            count += 1
        else:
            result += str(count) + temp
            temp = i
            count = 1
    print(result+str(count) + temp)
encoding(input())
