"""MAC Address"""
def mac(address):
    """Mac"""
    alpha_ = "A","a","B","b","C","c","D","d","E","e","F","f"
    symbol = ".","-",":"
    ans = ""
    for i in address:
        if i in alpha_ or i.isnumeric() or i in symbol:
            ans = "VALID"
        else:
            ans = "ERROR"
            break
    if ans == "ERROR":
        print(ans)
    else:
        if address[2::3] == "-----" and not "." in address and not ":" in address:
            ans = "VALID 1"
        elif address[2::3] == ":::::" and not "." in address and not "-" in address:
            ans = "VALID 2"
        elif address[4::5] == ".." and not ":" in address and not "-" in address:
            ans = "VALID 3"
        else:
            ans = "ERROR"
        print(ans)
mac(input())
