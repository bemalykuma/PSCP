'''Ascending Sort'''
def sorting(num):
    '''Ascending Sort'''
    number = []
    for _ in range(num):
        num_ = int(input())
        number.append(num_)
    number.sort()
    for i in number:
        print(i)
sorting(int(input()))
