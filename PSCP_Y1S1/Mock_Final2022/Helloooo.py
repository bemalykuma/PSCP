'''Helloooo'''
def helloooo(word):
    '''Helloooo'''
    vowel = "aeiou"
    add = word
    for i in range(1,len(word)+1):
        if word[-i] in vowel:
            c = word[len(word)-i+1:len(word)]
            if len(c) == 1 and c in vowel:
                c = ""
            add = word[:-i]+(word[-i]*4)+c
            break
    print(add)
helloooo(input())
