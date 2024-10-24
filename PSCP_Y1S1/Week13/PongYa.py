'''PongYa'''
def pong_ya(num):
    '''PongYa'''
    for i in range(1,num+1):
        ans = i
        if not i % 3 or str(num)[-1] == "3":
            ans = "PONG"
    print(ans)
pong_ya(int(input()))
