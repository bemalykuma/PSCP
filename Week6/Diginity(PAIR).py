"""Diginity"""
def diginity():
    """Diginity"""
    s = 0
    lst = []
    while True:
        num = input()
        f = num
        if int(num):
            while True:
                for i in f:
                    s += int(i)
                if s < 10:
                    break
                f = str(s)
                s = 0
            lst.append(s)
            s = 0
        else:
            break
    for j in lst:
        print(j)
diginity()
