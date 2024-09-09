"""Harshad"""
def harshad():
    """find harshad"""
    s = 0
    lst = []
    for _ in range(10):
        num = str(abs(int(input())))
        f = num
        for i in f:
            s += int(i)
        if not s:
            lst.append("No")
        elif not int(num) % s:
            lst.append("Yes")
        else:
            lst.append("No")
        s = 0
    for i in lst:
        print(i)
harshad()
