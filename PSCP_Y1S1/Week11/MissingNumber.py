'''MissingNumber'''
def missing(num):
    '''Find Missing Number'''
    all_num = set(range(1,num+1))
    num_set = set()
    n = 1
    while n > 0:
        n = int(input())
        num_set.add(n)
    for i in sorted(all_num - num_set):
        print(i)
missing(int(input()))
