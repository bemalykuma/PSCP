'''Digit v2'''
def digit(eng_num):
    '''Digit v2'''
    ten_11_12 = "twelve" in eng_num or "eleven" in eng_num or "ten" in eng_num
    if "thousand" in eng_num:
        print(4)
    elif "hundred" in eng_num:
        print(3)
    elif "teen" in eng_num or "ty" in eng_num or ten_11_12:
        print(2)
    else:
        print(1)
digit(input())
