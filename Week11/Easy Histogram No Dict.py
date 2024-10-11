'''Easy Histogram No Dict'''
def histogram(text):
    '''Easy Histogram No Dict'''
    text = list(i for i in text if i.isalpha())
    text.sort(key=lambda x: (x.lower(), x.isupper()))
    only_one = []
    for i in text:
        if not i in only_one:
            only_one.append(i)
    for i in only_one:
        print(i,"=",text.count(i))
histogram(input())
