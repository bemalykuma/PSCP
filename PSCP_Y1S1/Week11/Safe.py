'''Safe'''
def safe(lock, unlock):
    '''Safe'''
    answer = 0
    length = len(unlock)
    for i in range(length):
        if lock[i] != unlock[i]:
            ans = min(ord(lock[i]) - ord(unlock[i]), ord(unlock[i]) - ord(lock[i]))
            answer += min(abs(ans), ans + 26)
    print(answer)
safe(input(), input())
