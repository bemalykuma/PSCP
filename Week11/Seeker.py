'''Seeker'''
def seeker(code):
    '''Seeker'''
    i = 0
    ans = 0
    tmp = ""
    code = code + " "
    while i <= len(code)-1:
        if code[i].isdigit():
            tmp += code[i]
        elif i == len(code) or tmp:
            tmp = int(tmp)
            ans += tmp
            tmp = ""
        i += 1
    print(ans)
seeker(input())
