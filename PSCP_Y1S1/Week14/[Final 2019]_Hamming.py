'''Hamming'''
def ham(txt_1, txt_2):
    '''Hamming'''
    txt_1 = list(i for i in txt_1)
    txt_2 = list(i for i in txt_2)
    length, count = len(txt_1), 0
    for i in range(length):
        if txt_1[i] != txt_2[i]:
            count += 1
    print(count)
ham(input(), input())
