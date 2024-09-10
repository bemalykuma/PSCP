'''AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain'''
def find_vowels(text):
    '''AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain'''
    if "." in text:
        text = text.replace(".","")
    text = text.split()
    text.sort()
    ls = []
    for i in text:
        if i.count("a")+i.count("e")+i.count("i")+i.count("o")+i.count("u") > 1:
            ls.append(i)
    for i in ls:
        print(i)
    if not ls:
        print('Nope')
find_vowels(input())
