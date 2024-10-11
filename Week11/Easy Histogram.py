'''Easy Histogram'''
def histogram(text):
    '''Easy Histogram'''
    text = list(i for i in text if i.isalpha())
    text.sort(key=lambda x: (x.lower(), x.isupper()))
    cxunt_dict = dict.fromkeys(text, 0)
    for i in text:
        cxunt_dict[i] += 1
    for x, y in cxunt_dict.items():
        print(x, "=", y)
histogram(input())
