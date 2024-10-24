'''Gram_v1'''
def gram(text):
    '''gram'''
    word = ""
    dict_txt = {}
    for i in range(1,len(text)):
        word = text[i-1] + text[i]
        dict_txt[word] = (dict_txt[word] + 1 if word in dict_txt else 1)
    max_val = max(dict_txt.values())
    for i in dict_txt.items():
        if i[1] == max_val:
            print(i[0])
            print(i[1])
            break
gram(input())
