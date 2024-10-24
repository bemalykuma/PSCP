'''Inverter'''
def inverter(binary):
    '''Inverter'''
    ans = ""
    for i in binary:
        if i == "1":
            ans += "0"
        else:
            ans += "1"
    if int(ans):
        print(int(ans))
inverter(input())
