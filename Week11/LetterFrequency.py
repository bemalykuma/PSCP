'''LetterFrequency'''
def letter(text):
    '''LetterFrequency'''
    data = {}
    for i in text:
        if i.isalpha():
            data[i] = 0
    for i in text:
        if i.isalpha():
            data[i] += 1
    alpha_lst = list(data.keys())
    count_lst = list(data.values())
    print(alpha_lst[count_lst.index(max(count_lst))])
letter(input().lower())
