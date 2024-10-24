'''Socks'''
def socks(sock):
    '''Socks'''
    sock_lst = list(i for i in sock)
    sock_lst.sort()
    ans = ''
    temp = ''
    count = 0
    for i in sock_lst:
        temp += i
        if len(temp) == 2:
            if temp[1] != temp[0]:
                temp = temp[1]
            else:
                ans += temp + " "
                temp = ''
                count += 1
    if not ans:
        ans = "None"
    print(ans)
    print(count)
socks(input())
