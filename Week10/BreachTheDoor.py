'''BreachTheDoor'''
def longer_6ix(text):
    '''BreachTheDoor'''
    var_1 = ""
    txt_lst = []
    for i in text:
        if i.isalpha() or i == " ":
            var_1 += i
    txt_lst = var_1.split()
    for i in txt_lst:
        length_txt = len(i)
        if length_txt > 6:
            print(i,end=' ')
longer_6ix(input())
