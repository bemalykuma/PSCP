'''MissingNumber No Set'''
def missing(num):
    '''Find Missing Number'''
    num_lst = []
    n = 1
    while n > 0:
        n = int(input())
        num_lst.append(n)
    for i in range(1,num+1):
        if not i in num_lst:
            print(i)
missing(int(input()))
