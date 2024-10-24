'''IP Address'''
def ip_address(ip):
    '''Valid or Invalid'''
    cond_dot = ".." in ip or "..." in ip or ip[0] == "." or ip[-1] == "."
    invalid = 0
    for i in ip:
        if i == "." or i.isnumeric():
            invalid += 0
        else:
            invalid += 1
    if invalid > 0 or ip.count(".") != 3 or cond_dot:
        print("Invalid IPv4 address")
        return
    lst_ip = ip.split(".")
    ans = []
    for i in lst_ip:
        i = int(i)
        if i > 255:
            print("Invalid IPv4 address")
            return
        ans.append(str(i))
    print(".".join(ans))
ip_address(input())
