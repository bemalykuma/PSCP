"""NumberMassage"""
def trans(n):
    """Trans number to alpha"""
    if n == "1":
        ans = n.replace("1","I")
    elif n == "3":
        ans = n.replace("3","E")
    elif n == "4":
        ans = n.replace("4","A")
    elif n == "5":
        ans = n.replace("5","S")
    elif n == "0":
        ans = n.replace("0","O")
    else:
        ans = ""
    return ans

def massage(text):
    """Number massage"""
    result = text
    answer = ""
    if "12" in result:
        result = result.replace("12","R")
    if "13" in result:
        result = result.replace("13","B")
    for i in result:
        if i in ("1","3","4","5","0"):
            i = trans(i)
            answer += i
        elif i.isalpha() or i == " ":
            answer += i
        else:
            answer += ""
    print(answer.upper())
massage(input())
