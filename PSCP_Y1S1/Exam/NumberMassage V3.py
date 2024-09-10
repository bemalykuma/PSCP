"""NumberMassage"""
def massage(text):
    """Number massage"""
    text = text.replace("12","R").replace("13","B").replace("1","I").replace("3","E")\
        .replace("4","A").replace("5","S").replace("0","O").upper()
    for i in text:
        if i in (2,6,7,8,9):
            text = text.replace(i,"")
    print(text)
massage(input())
