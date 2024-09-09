'''Backward'''
def back():
    '''Backward'''
    text = input()
    ls = []
    while text != "NULL":
        ls.append(text)
        text = input()
    ls.reverse()
    for i in ls:
        print(i)
back()
