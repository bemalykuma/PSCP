'''Matrix_MN'''
def matrix(m, n):
    '''Matrix_MN'''
    ans = ''
    j = 0
    for _ in range(m * n):
        num = input()
        ans += num + ' '
        j += 1
        if not j % n:
            print(ans[:-1], end="")
            print()
            ans = ''
matrix(int(input()), int(input()))
