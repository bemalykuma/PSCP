'''Calculator V2'''
def length(x):
    '''length'''
    ans = len(str(x)) + len(str(length(x-1)))
    if x < 1:
        return ans
    else:
        ans = len(str(x))
        x -= 1
        ans += len(str(length(x)))
        return ans

def cal(num):
    '''Calculator V2'''
    print(length(num))
cal(int(input()))
